from django.core.management.base import BaseCommand
from portfolio.models import Skill, Project, Experience, Education, Certification, Achievement

class Command(BaseCommand):
    help = 'Seeds the database with Deepanshu Chauhan\'s portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding portfolio data...')

        # Clear existing data to avoid duplicates on re-run
        Skill.objects.all().delete()
        Project.objects.all().delete()
        Experience.objects.all().delete()
        Education.objects.all().delete()
        Certification.objects.all().delete()
        Achievement.objects.all().delete()

        # 1. Seed Skills
        skills_data = [
            # Programming Languages
            ('Python', 'languages', 95, 'devicon-python-plain colored', 1),
            ('JavaScript', 'languages', 85, 'devicon-javascript-plain colored', 2),
            
            # Frontend
            ('HTML5', 'frontend', 90, 'devicon-html5-plain colored', 1),
            ('CSS3', 'frontend', 88, 'devicon-css3-plain colored', 2),
            ('JavaScript (ES6+)', 'frontend', 85, 'devicon-javascript-plain colored', 3),
            ('Responsive Web Design', 'frontend', 92, 'devicon-chrome-plain colored', 4),
            
            # Backend
            ('Django', 'backend', 95, 'devicon-django-plain colored', 1),
            ('Flask', 'backend', 80, 'devicon-flask-original colored', 2),
            ('FastAPI', 'backend', 85, 'devicon-fastapi-plain colored', 3),
            ('REST APIs', 'backend', 92, 'devicon-fastapi-plain colored', 4),
            ('JWT Authentication', 'backend', 90, 'devicon-google-plain colored', 5),
            
            # Databases
            ('PostgreSQL', 'database', 88, 'devicon-postgresql-plain colored', 1),
            ('MySQL', 'database', 85, 'devicon-mysql-plain colored', 2),
            ('MongoDB', 'database', 80, 'devicon-mongodb-plain colored', 3),
            
            # AI Development
            ('Prompt Engineering', 'ai_development', 95, 'devicon-chrome-plain colored', 1),
            ('ChatGPT API Integration', 'ai_development', 92, 'devicon-chrome-plain colored', 2),
            ('Claude API', 'ai_development', 90, 'devicon-chrome-plain colored', 3),
            ('Gemini API', 'ai_development', 92, 'devicon-google-plain colored', 4),
            ('Cursor AI', 'ai_development', 95, 'devicon-vscode-plain colored', 5),
            ('LLM Integration', 'ai_development', 90, 'devicon-chrome-plain colored', 6),
            ('AI Workflow Automation', 'ai_development', 88, 'devicon-chrome-plain colored', 7),
            ('AI-Assisted Debugging', 'ai_development', 94, 'devicon-chrome-plain colored', 8),
            
            # DevOps
            ('Docker', 'devops', 85, 'devicon-docker-plain colored', 1),
            ('Git', 'devops', 90, 'devicon-git-plain colored', 2),
            ('GitHub', 'devops', 92, 'devicon-github-original colored', 3),
            ('Render', 'devops', 85, 'devicon-chrome-plain colored', 4),
            ('Vercel', 'devops', 80, 'devicon-chrome-plain colored', 5),
            
            # Computer Science Fundamentals
            ('Data Structures & Algorithms', 'computer_science', 88, 'devicon-cplusplus-plain colored', 1),
            ('Object-Oriented Programming', 'computer_science', 90, 'devicon-python-plain colored', 2),
            ('Database Management System (DBMS)', 'computer_science', 85, 'devicon-postgresql-plain colored', 3),
            ('Operating Systems', 'computer_science', 82, 'devicon-linux-plain colored', 4),
            ('Computer Networks', 'computer_science', 80, 'devicon-chrome-plain colored', 5),
            ('Software Engineering Principles', 'computer_science', 88, 'devicon-chrome-plain colored', 6),
        ]

        for name, category, prof, icon, order in skills_data:
            Skill.objects.create(name=name, category=category, proficiency=prof, icon_class=icon, display_order=order)

        # 2. Seed Projects
        p1 = Project.objects.create(
            title='AI Healthcare Assistant',
            description='An intelligent AI-powered healthcare assistant designed to streamline patient triaging, automate appointment scheduling, and provide secure medicine tracking.',
            detailed_description='AI Healthcare Assistant is a premium web application developed to bridge the gap between patients and doctors. It utilizes advanced AI models (Gemini API Ready) to assist patients in understanding their symptoms, booking appointments with matching healthcare professionals, and securely maintaining digital medical records. The application hosts a dedicated Patient Dashboard, an intuitive Doctor Portal with calendar schedules, and a comprehensive Admin Panel for medical coordinators.',
            tech_stack='Python, Django, Django REST Framework, Gemini API, SQLite, JWT, Docker',
            key_features='AI-Driven Symptom Chatbot\nPatient Dashboard with appointment scheduler\nDoctor Calendar and consultation dashboard\nSecure electronic health records (EHR) vault\nAutomated daily medicine reminders\nJWT-based API authentication\nFully Dockerized environment',
            challenges_faced='Managing data security and ensuring HIPAA-compliant design patterns for patient electronic records. Solved by integrating strict encryption layers and robust session/JWT tokens. Another challenge was minimizing latency during LLM prompt evaluation; resolved by setting up structured prompt contexts and local caching for common medical queries.',
            future_improvements='Deploying real-time WebRTC based video consultation rooms directly within the dashboard. Integrating smart wearable devices APIs (such as Fitbit and Apple Health) to continuously monitor vitals.',
            github_link='https://github.com/DeepanshuChauhan4422/ai-healthcare-assistant',
            live_demo_link='https://ai-healthcare-assistant-ivio.onrender.com',
            is_featured=True,
            display_order=1
        )

        p2 = Project.objects.create(
            title='Team Task Manager',
            description='A dynamic, responsive project management portal enabling fluid team collaboration, task assignment, progress tracking, and deadline monitoring.',
            detailed_description='Team Task Manager is a full-featured collaborative application designed to improve organizational productivity. The platform lets managers create team workspaces, assign granular tasks, track progress via visual indicators, and monitor impending deadlines. Team members can comment, submit work, and update statuses interactively. The app is crafted with a mobile-first philosophy, ensuring smooth execution across all screen sizes.',
            tech_stack='Python, Django, Vanilla JavaScript, HTML5, CSS3, PostgreSQL, Docker',
            key_features='Team Workspaces and workspace dashboards\nTask Assignment with priority and deadline markers\nInteractive progress bars and board views\nSecure user auth and authorization checks\nInternal message board for workspace updates\nFully responsive CSS grid and flexbox layout\nContainerized with Docker Compose',
            challenges_faced='Creating a clean, responsive drag-and-drop or state-updating interface without importing bloated front-end frameworks. Handled by building custom lightweight vanilla JavaScript handlers interacting with Django REST endpoints via fetch requests, delivering instant visual updates while preserving MVT structure.',
            future_improvements='Implementing real-time WebSockets notifications with Django Channels to sync task updates across active users without manual refreshes. Adding interactive Gantt charts and analytics dashboards.',
            github_link='https://github.com/DeepanshuChauhan4422/team-task-manager',
            live_demo_link='https://team-task-manager-n72w.onrender.com/',
            is_featured=True,
            display_order=2
        )

        p3 = Project.objects.create(
            title='Real Estate Price Prediction',
            description='An AI-powered property analytics tool that leverages machine learning models to search, filter, and predict real estate valuations based on regional factors.',
            detailed_description='Real Estate Price Prediction application integrates data science with full-stack development to deliver property estimates. The platform allows users to search properties across different cities and filter them based on specifications. The core features a trained Machine Learning model (linear regression / gradient boosting) which evaluates multiple attributes (size, rooms, location, age, proximity to transit) to predict a realistic market price.',
            tech_stack='Python, Flask, Django, Scikit-learn, Pandas, NumPy, Bootstrap, PostgreSQL',
            key_features='Interactive property search and filtration system\nML regression model predicting real estate value\nData visualization charts for price trends\nREST API serving model predictions dynamically\nGeographical location filtering',
            challenges_faced='Cleaning dirty real estate datasets containing missing values and skewed geographical locations. Handled by implementing robust preprocessing pipelines in Pandas/NumPy, applying one-hot encoding for categorical coordinates, and using robust scaling to minimize outlier influences on the machine learning algorithm.',
            future_improvements='Integrating Google Maps API to visually display properties on a map with price-range contours. Transitioning to advanced neural network models for even higher prediction accuracy.',
            github_link='https://github.com/DeepanshuChauhan4422/real-estate-prediction',
            live_demo_link='https://real-estate-price-prediction-omega.vercel.app/',
            is_featured=True,
            display_order=3
        )

        # 3. Seed Experience
        Experience.objects.create(
            company='HCL Technologies',
            role='IT Trainee',
            duration='',
            description='Completed comprehensive Industry Training focused on enterprise software workflows.\nApplied algorithmic problem-solving to practical programming challenges.\nCollaborated in agile team settings to build prototype modules.\nHoned professional communication skills and technical documentation standards.\nReceived hands-on exposure to practical software development lifecycles (SDLC).',
            display_order=1
        )

        # 4. Seed Education
        Education.objects.create(
            institution='KCC Institute of Technology and Management',
            degree='Bachelor of Technology (B.Tech)',
            branch='Computer Science & Engineering (Artificial Intelligence & Machine Learning)',
            duration='2022 to 2026',
            academic_journey='Pursued CS with a specialization in AI and Machine Learning. Acquired deep understanding of fundamental computer science, software engineering principles, algorithms, and deep learning neural structures. Developed multiple academic applications focusing on integrating web frameworks with intelligent model APIs.',
            display_order=1
        )

        # 5. Seed Certifications
        Certification.objects.create(
            title='HCL Technologies Industry Training Certification',
            issuing_organization='HCL Technologies',
            issue_date='August 2024',
            credential_id='HCL-TR-2024-897',
            display_order=1
        )
        Certification.objects.create(
            title='AICTE SANKALP HPC Workshop Participant Certificate',
            issuing_organization='AICTE & SANKALP',
            issue_date='March 2024',
            credential_id='AICTE-HPC-WORK-445',
            display_order=2
        )

        # 6. Seed Achievements
        Achievement.objects.create(
            title='4th Rank in SANKALAN Code Auction',
            description='Secured 4th Rank in the prestigious SANKALAN Code Auction coding competition, competing against several developers to optimize code bases under constraints.',
            ranking_details='4th Rank out of 300+ teams',
            display_order=1
        )
        Achievement.objects.create(
            title='HCL Certified IT Trainee',
            description='Recognized for exceptional project delivery and conceptual clarity during the HCL Technologies training program.',
            ranking_details='Certified with distinction',
            display_order=2
        )
        Achievement.objects.create(
            title='AICTE SANKALP High Performance Computing Participant',
            description='Completed intensive workshop training on High Performance Computing and cluster parallelism systems organized by AICTE.',
            ranking_details='Official Participant',
            display_order=3
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded all portfolio data!'))
