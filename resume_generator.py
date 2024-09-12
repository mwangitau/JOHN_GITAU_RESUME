import html

def escape_html(text):
    return html.escape(text)

class ResumeBuilder:
    def __init__(self):
        self.html = []

    def add(self, content):
        self.html.append(content)

    def build(self):
        return "\n".join(self.html)

# Add this projects list before the generate_resume() function
projects = [
    {
        "name": "R Data Analysis Portfolio: Kenya Malaria Infection",
        "description": "Comprehensive analysis of malaria infection rates in Kenya using R, demonstrating proficiency in data manipulation, visualization, and statistical analysis.",
        "link": "r_portfolio.html"
    },
    # Add more projects here as needed
]


def generate_resume():
    resume = ResumeBuilder()

    # HTML structure
    resume.add("<!DOCTYPE html>")
    resume.add("<html lang='en'>")
    resume.add("<head>")
    resume.add("    <meta charset='UTF-8'>")
    resume.add("    <meta name='viewport' content='width=device-width, initial-scale=1.0'>")
    resume.add("    <title>John Gitau - Statistician</title>")
    resume.add("    <script src='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/js/all.min.js'></script>")
    resume.add("    <style>")
    resume.add("""
        :root {
            --primary-color: #2c3e50;
            --secondary-color: #3498db;
            --text-color: #333;
            --background-color: #f4f4f4;
        }
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--background-color);
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        header {
            background-color: var(--primary-color);
            color: #fff;
            text-align: center;
            padding: 2rem 0;
        }
        h1 { font-size: 2.5rem; margin-bottom: 0.5rem; }
        h2 {
            font-size: 1.8rem;
            margin-bottom: 1rem;
            color: var(--secondary-color);
        }
        .contact-info {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 1rem;
        }
        .contact-info a {
            color: #fff;
            text-decoration: none;
        }
        main { padding: 2rem 0; }
        section { margin-bottom: 2rem; }
        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        .skill {
            background-color: var(--secondary-color);
            color: #fff;
            padding: 0.5rem 1rem;
            border-radius: 20px;
            font-size: 0.9rem;
        }
        .experience-item, .education-item { margin-bottom: 1.5rem; }
        .experience-item h3, .education-item h3 { margin-bottom: 0.5rem; }
        .experience-item p, .education-item p { margin-bottom: 0.25rem; }
        ul { padding-left: 1.5rem; }
        footer {
            background-color: var(--primary-color);
            color: #fff;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
        .language-item {
            margin-bottom: 1rem;
        }
        .language-name {
            font-weight: bold;
            margin-bottom: 0.25rem;
        }
        .proficiency-bar {
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            overflow: hidden;
        }
        .proficiency-level {
            height: 100%;
            background-color: var(--secondary-color);
        }
        .project-item {
            margin-bottom: 1.5rem;
        }
        .project-item h3 {
            margin-bottom: 0.5rem;
        }
        .project-link {
            display: inline-block;
            padding: 0.5rem 1rem;
            background-color: var(--secondary-color);
            color: #fff;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 0.5rem;
            transition: background-color 0.3s;
        }
        .project-link:hover {
            background-color: #2980b9;
        }

        @media (max-width: 768px) {
            h1 { font-size: 2rem; }
            h2 { font-size: 1.5rem; }
        }
    """)
    resume.add("    </style>")
    resume.add("</head>")
    resume.add("<body>")

    # Header
    resume.add("    <header>")
    resume.add("        <div class='container'>")
    resume.add("            <h1>John Gitau</h1>")
    resume.add("            <p>Statistician</p>")
    resume.add("            <div class='contact-info'>")
    resume.add("                <a href='mailto:mwangijohngitau1@gmail.com'><i class='fas fa-envelope'></i> mwangijohngitau1@gmail.com</a>")
    resume.add("                <a href='tel:+254717034328'><i class='fas fa-phone'></i> +254 717 034 328</a>")
    resume.add("                <a href='https://www.linkedin.com/in/john-mwangi-09b482113' target='_blank'><i class='fab fa-linkedin'></i> LinkedIn</a>")
    resume.add("                <a href='https://github.com/mwangitau' target='_blank'><i class='fab fa-github'></i> GitHub</a>")
    resume.add("            </div>")
    resume.add("        </div>")
    resume.add("    </header>")

    # Main content
    resume.add("    <main class='container'>")

    # Profile
    resume.add("        <section id='profile'>")
    resume.add("            <h2>Profile</h2>")
    resume.add(f"            <p>{escape_html('Detail-oriented statistician with a BSc in Applied Statistics with IT. Proficient in Python, R, SQL, and cloud platforms like Google Cloud and AWS. Skilled in data analysis, visualization (ggplot2, matplotlib, Seaborn), and management. Experienced in research, quality assurance, and project management with Asana. Strong problem-solving, communication, and time management skills. Certified in SEO and digital skills.')}</p>")
    resume.add("        </section>")

    # Skills
    resume.add("        <section id='skills'>")
    resume.add("            <h2>Skills</h2>")
    resume.add("            <div class='skills'>")
    skills = ["Python", "R", "SQL", "Data Analysis", "Data Visualization", "Git", "Linux", "Asana", "Google Cloud", "AWS", "Problem-Solving", "Communication"]
    for skill in skills:
        resume.add(f"                <span class='skill'>{escape_html(skill)}</span>")
    resume.add("            </div>")
    resume.add("        </section>")

    # Projects
    resume.add("        <section id='projects'>")
    resume.add("            <h2>Projects</h2>")
    for project in projects:
        resume.add("            <div class='project-item'>")
        resume.add(f"                <h3>{escape_html(project['name'])}</h3>")
        resume.add(f"                <p>{escape_html(project['description'])}</p>")
        resume.add(f"                <a href='{escape_html(project['link'])}' target='_blank' class='project-link'>View Project</a>")
        resume.add("            </div>")
    resume.add("        </section>")


    # Languages
    resume.add("        <section id='languages'>")
    resume.add("            <h2>Languages</h2>")
    languages = [
        {"name": "English", "proficiency": 90},
        {"name": "Swahili", "proficiency": 100},
        {"name": "Duetsch", "proficiency": 20}
    ]
    for lang in languages:
        resume.add("            <div class='language-item'>")
        resume.add(f"                <div class='language-name'>{escape_html(lang['name'])}</div>")
        resume.add("                <div class='proficiency-bar'>")
        resume.add(f"                    <div class='proficiency-level' style='width: {lang['proficiency']}%;'></div>")
        resume.add("                </div>")
        resume.add("            </div>")
    resume.add("        </section>")

    # Achievements
    resume.add("        <section id='achievements'>")
    resume.add("            <h2>Achievements</h2>")
    achievements = [
        {"name": "Customer Trust and Loyalty", "percentage": 90},
        {"name": "Compliance with Safety Standards", "percentage": 100},
        {"name": "Operational Efficiency", "percentage": 85},
        {"name": "Staff Productivity", "percentage": 80}
    ]
    for achievement in achievements:
        resume.add("            <div class='achievement-item'>")
        resume.add(f"                <div class='achievement-name'>{escape_html(achievement['name'])}</div>")
        resume.add("                <div class='achievement-bar'>")
        resume.add(f"                    <div class='achievement-level' style='width: {achievement['percentage']}%;'></div>")
        resume.add("                </div>")
        resume.add(f"                <div class='achievement-percentage'>{achievement['percentage']}%</div>")
        resume.add("            </div>")
    resume.add("        </section>")

    # Work Experience
    resume.add("        <section id='experience'>")
    resume.add("            <h2>Work Experience</h2>")
    experiences = [
        {
            "title": "Quality Marshall",
            "company": "Shell Service Station, Joska, Machakos, KENYA",
            "period": "2022-2024",
            "responsibilities": [
                "Maintain product and service quality, including fuel, lubricants, and customer service.",
                "Ensure adherence to Shell's standards, safety regulations, and legal requirements.",
                "Provide excellent customer service, address inquiries, and resolve issues promptly.",
                "Train staff on operational procedures, safety, and product knowledge regularly.",
                "Monitor and replenish fuel and product stock levels."
            ]
        },
        {
            "title": "Research Statistician (Internship)",
            "company": "Kenya Agricultural and Livestock Research Institute, Kakamega, KENYA",
            "period": "September 2021 - December 2021",
            "responsibilities": [
                "Collaborated with researchers to design experiments and field trials, ensuring statistical validity.",
                "Oversaw agricultural and livestock data collection, ensuring accuracy and completeness.",
                "Conducted statistical analyses using techniques like regression analysis and ANOVA.",
                "Developed predictive models for agricultural and livestock outcomes using machine learning techniques."
            ]
        },
        {
            "title": "Data Entry Clerk",
            "company": "Mang'u Credit Union, Mang'u, Kiambu, Kenya",
            "period": "March 2018 - August 2018",
            "responsibilities": [
                "Ensured precise input of financial data like deposits and withdrawals into the credit union's database.",
                "Updated and managed member information, including personal details and account data.",
                "Handled account actions like openings, closings, and transfers following established procedures.",
                "Generated reports based on financial data for analysis, auditing, and decision-making purposes."
            ]
        }
    ]
    for exp in experiences:
        resume.add("            <div class='experience-item'>")
        resume.add(f"                <h3>{escape_html(exp['title'])}</h3>")
        resume.add(f"                <p>{escape_html(exp['company'])}</p>")
        resume.add(f"                <p>{escape_html(exp['period'])}</p>")
        resume.add("                <ul>")
        for resp in exp['responsibilities']:
            resume.add(f"                    <li>{escape_html(resp)}</li>")
        resume.add("                </ul>")
        resume.add("            </div>")
    resume.add("        </section>")

    # Education
    resume.add("        <section id='education'>")
    resume.add("            <h2>Education</h2>")
    educations = [
        {
            "degree": "Bachelor of Science (Applied Statistics with IT)",
            "school": "Kaimosi Friends University",
            "period": "2017-2023"
        },
        {
            "degree": "Kenya Certificate of Secondary Education",
            "school": "Karura SDA Secondary School",
            "period": "2013-2015"
        },
        {
            "degree": "Kenya Certificate of Primary Education",
            "school": "Kamwangi Morning Glory",
            "period": "2007-2010"
        }
    ]
    for edu in educations:
        resume.add("            <div class='education-item'>")
        resume.add(f"                <h3>{escape_html(edu['degree'])}</h3>")
        resume.add(f"                <p>{escape_html(edu['school'])}</p>")
        resume.add(f"                <p>{escape_html(edu['period'])}</p>")
        resume.add("            </div>")
    resume.add("        </section>")

    # Certifications
    resume.add("        <section id='certifications'>")
    resume.add("            <h2>Certifications</h2>")
    resume.add("            <ul>")
    certifications = [
        "Health Safety Security and Environment Certification - 2023",
        "Clean and Safe Certification - 2023",
        "Search Engine Optimization Certification by Coursera - 2021",
        "Google Africa Developer Program by Google Cloud - 2021",
        "Digital Skills by Cloud Factory - 2020"
    ]
    for cert in certifications:
        resume.add(f"                <li>{escape_html(cert)}</li>")
    resume.add("            </ul>")
    resume.add("        </section>")

    resume.add("    </main>")

    # Footer
    resume.add("    <footer>")
    resume.add("        <div class='container'>")
    resume.add("            <p>&copy; 2024 John Gitau. All rights reserved.</p>")
    resume.add("        </div>")
    resume.add("    </footer>")

    # JavaScript
    resume.add("    <script>")
    resume.add("""
        document.addEventListener('DOMContentLoaded', function() {
            const skillsSection = document.querySelector('#skills');
            const skills = skillsSection.querySelectorAll('.skill');

            skills.forEach(skill => {
                skill.addEventListener('mouseover', function() {
                    this.style.transform = 'scale(1.1)';
                    this.style.transition = 'transform 0.3s ease';
                });

                skill.addEventListener('mouseout', function() {
[O                    this.style.transform = 'scale(1)';
                });
            });
        });
    """)
    resume.add("    </script>")

    resume.add("</body>")
    resume.add("</html>")

    return resume.build()

import qrcode

# URL of the resume
resume_url = "https://mwangitau.github.io/JOHN_GITAU_RESUME/"

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add the resume URL to the QR code
qr.add_data(resume_url)
qr.make(fit=True)

# Create an image from the QR code
qr_image = qr.make_image(fill='black', back_color='white')

# Save the QR code image
qr_image.save("JOHN_GITAU_RESUME_QR_CODE.png")

print("QR Code generated and saved as 'JOHN_GITAU_RESUME_QR_CODE.png'")


# Generate the resume HTML
resume_html = generate_resume()

# Write the HTML to a file
with open("john_gitau_resume.html", "w", encoding="utf-8") as f:
    f.write(resume_html)

print("Resume HTML file 'john_gitau_resume.html' has been generated successfully.")
