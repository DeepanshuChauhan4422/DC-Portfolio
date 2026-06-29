import os
import json
from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.utils.decorators import method_decorator
from django.utils import timezone
from .models import (
    Skill, Project, Experience, Education, Certification, Achievement, ContactMessage
)

# Optional imports for AI
try:
    import google.generativeai as genai
except ImportError:
    genai = None

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class HomeView(View):
    def get(self, request):
        skills = Skill.objects.all()
        projects = Project.objects.filter(is_featured=True)
        experiences = Experience.objects.all()
        educations = Education.objects.all()
        certifications = Certification.objects.all()
        achievements = Achievement.objects.all()

        # Group skills by category for easier rendering in sections
        grouped_skills = {
            'languages': skills.filter(category='languages'),
            'frontend': skills.filter(category='frontend'),
            'backend': skills.filter(category='backend'),
            'database': skills.filter(category='database'),
            'ai_development': skills.filter(category='ai_development'),
            'devops': skills.filter(category='devops'),
            'computer_science': skills.filter(category='computer_science'),
        }

        context = {
            'grouped_skills': grouped_skills,
            'projects': projects,
            'experiences': experiences,
            'educations': educations,
            'certifications': certifications,
            'achievements': achievements,
            'github_username': os.getenv('GITHUB_USERNAME', 'DeepanshuChauhan4422'),
            'current_year': timezone.now().year,
        }
        return render(request, 'portfolio/index.html', context)


@method_decorator(ensure_csrf_cookie, name='dispatch')
class ContactMessageView(View):
    def post(self, request):
        try:
            # Handle AJAX request
            data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
            
            name = data.get('name', '').strip()
            email = data.get('email', '').strip()
            subject = data.get('subject', '').strip()
            message = data.get('message', '').strip()

            if not (name and email and subject and message):
                return JsonResponse({
                    'status': 'error',
                    'message': 'All fields (Name, Email, Subject, Message) are required.'
                }, status=400)

            # Create message record
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )

            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent successfully. Deepanshu will get back to you shortly!'
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'An unexpected error occurred: {str(e)}'
            }, status=500)


class AIAssistantView(View):
    def post(self, request):
        try:
            data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
            user_message = data.get('message', '').strip()

            if not user_message:
                return JsonResponse({
                    'status': 'error',
                    'message': 'Query message cannot be empty.'
                }, status=400)

            # Build resume profile context
            context_prompt = self._get_profile_context()

            # Attempt to use configured LLM APIs
            response_text = None
            gemini_key = os.getenv('GEMINI_API_KEY')
            openai_key = os.getenv('OPENAI_API_KEY')

            if gemini_key and genai:
                try:
                    genai.configure(api_key=gemini_key)
                    # Use gemini-1.5-flash or gemini-2.5-flash
                    model = genai.GenerativeModel('gemini-1.5-flash')
                    full_prompt = f"{context_prompt}\n\nVisitor's Question: {user_message}\n\nAI Assistant Response:"
                    response = model.generate_content(full_prompt)
                    response_text = response.text.strip()
                except Exception as ex:
                    # Log exception and fallback
                    print(f"Gemini API Error: {str(ex)}")

            if not response_text and openai_key and OpenAI:
                try:
                    client = OpenAI(api_key=openai_key)
                    completion = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": context_prompt},
                            {"role": "user", "content": user_message}
                        ]
                    )
                    response_text = completion.choices[0].message.content.strip()
                except Exception as ex:
                    print(f"OpenAI API Error: {str(ex)}")

            # Fallback to local keyword matcher if no LLM responded
            if not response_text:
                response_text = self._fallback_response(user_message)

            return JsonResponse({
                'status': 'success',
                'response': response_text
            })

        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Server error: {str(e)}'
            }, status=500)

    def _get_profile_context(self):
        """Constructs a factual context representing Deepanshu Chauhan's resume."""
        return """
You are the interactive AI Portfolio Assistant representing Deepanshu Chauhan on his personal website.
Your job is to answer the visitor's questions about Deepanshu in a highly professional, helpful, and concise manner.
Keep your answers brief (1-3 sentences or small bullet points where appropriate) and maintain a friendly, engaging developer-copilot persona.

Here are the facts about Deepanshu:
- **Full Name**: Deepanshu Chauhan
- **Role**: Full Stack Developer | AI Application Developer | Software Engineer
- **Core Tagline**: Building intelligent, scalable, and modern web applications with Python, Django, AI, and modern web technologies.
- **Location**: Greater Noida, India
- **Education**: B.Tech in Computer Science & Engineering (Specialization in AI & Machine Learning) from KCC Institute of Technology and Management (2022-2026).
- **Core Technical Stack**:
  - Languages: Python, JavaScript, HTML5, CSS3.
  - Backend: Django, FastAPI, Flask, REST APIs, JWT Auth.
  - Databases: PostgreSQL, MySQL, MongoDB.
  - AI Dev: Prompt Engineering, LLM Integration (Gemini, OpenAI), AI Workflow Automation, Cursor AI, MCP.
  - DevOps: Docker, Git, GitHub, Render, Vercel.
- **Experience**:
  - HCL Technologies - IT Trainee. Focused on industry training, coding solutions, and team workflows.
- **Projects**:
  1. *AI Healthcare Assistant*: Django MVT backend, Gemini API chatbot for symptom triaging, doctor/patient portals, and Dockerized deployment.
  2. *Team Task Manager*: Collaboration workspace with dashboards, task assignment, progress tracks, and vanilla CSS/JS responsive frontend.
  3. *Real Estate Price Prediction*: ML regression model in Scikit-learn with Flask/Django backend predicting property prices.
- **Certifications & Achievements**:
  - 4th Rank in SANKALAN Code Auction.
  - AICTE SANKALP High Performance Computing (HPC) Workshop Participant.
  - HCL Certified IT Trainee.
- **Hiring pitch**: Deepanshu enjoys solving architectural challenges, creating elegant backend databases/APIs, and deploying custom AI agents. He is passionate, quick to adapt, and brings specialized AI/ML skills to a standard web stack.
"""

    def _fallback_response(self, message):
        """Standard responsive keyword classifier if Gemini or ChatGPT is not active."""
        msg = message.lower()
        
        # Greet
        if any(w in msg for w in ['hello', 'hi', 'hey', 'greetings', 'hola']):
            return ("Hi there! I am Deepanshu's AI Portfolio Assistant. "
                    "I can answer questions about Deepanshu's skills, professional experience, projects, or education. What would you like to know?")
        
        # Skills
        if 'skills' in msg or 'skill' in msg or 'technologies' in msg or 'languages' in msg or 'stack' in msg:
            return ("Deepanshu is highly proficient in Python, Django, FastAPI, Flask, and JavaScript. "
                    "He also works extensively with PostgreSQL, Docker, Git, and integrating AI models like Gemini and Claude.")
        
        # Projects
        if 'project' in msg or 'portfolio' in msg or 'work' in msg:
            return ("Deepanshu has built several featured projects: \n"
                    "1. **AI Healthcare Assistant**: Django-based portal with Gemini API symptom chatbot.\n"
                    "2. **Team Task Manager**: Workspace dashboard for collaboration.\n"
                    "3. **Real Estate Price Prediction**: ML model predicting property valuations.")

        # Experience
        if 'experience' in msg or 'work' in msg or 'hcl' in msg or 'job' in msg:
            return ("Deepanshu worked as an IT Trainee at HCL Technologies, where he gained practical industry exposure, "
                    "honed coding skills, and collaborated in agile workflows.")

        # Education
        if 'education' in msg or 'college' in msg or 'university' in msg or 'study' in msg or 'degree' in msg:
            return ("Deepanshu is pursuing a B.Tech in Computer Science & Engineering (specializing in AI & Machine Learning) from KCC Institute of Technology and Management (2022-2026).")

        # Contact/Hire
        if 'contact' in msg or 'hire' in msg or 'email' in msg or 'resume' in msg:
            return ("You can get in touch with Deepanshu by filling out the Contact Form below, emailing him directly, or checking out his GitHub and LinkedIn profiles! "
                    "I can assure you he is ready to build scalable, intelligent software for your team.")

        # AI
        if 'ai' in msg or 'gemini' in msg or 'chatgpt' in msg:
            return ("Deepanshu develops AI-integrated solutions! His projects use Prompt Engineering, LLM APIs (Gemini/OpenAI), and automated workflows.")

        # Default fallback
        return ("I am Deepanshu's portfolio assistant. He is a Full Stack & AI Developer specializing in Python, Django, and AI integrations. "
                "Feel free to ask about his skills, experience at HCL, or his AI Healthcare Assistant project!")
