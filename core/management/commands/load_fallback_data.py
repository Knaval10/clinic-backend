import os
from django.core.management.base import BaseCommand

from apps.homepage.models import HomePage
from apps.doctors.models import Doctor
from apps.testimonials.models import Testimonial
from apps.services.models import Service

class Command(BaseCommand):
    help = 'Populates the database with fallback data manually'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Starting to load fallback data..."))

        # 1. HomePage Data
        fallbackHomeData = [
            {
                "title": "Hridaya Dental Clinic",
                "subtitle": "Where Every Smile Is Treated with Heart",
                "description": "We provide comprehensive dental services with a team of experienced dental professionals dedicated to your oral health and confident smile.",
            },
            {
                "title": "Expert Dental Care",
                "subtitle": "Advanced Technology, Compassionate Service",
                "description": "Our state-of-the-art facilities and dedicated team ensure you receive the best dental treatment possible.",
            },
        ]
        HomePage.objects.all().delete()
        for idx, slide in enumerate(fallbackHomeData, 1):
            HomePage.objects.create(
                title=slide["title"],
                subtitle=slide["subtitle"],
                description=slide["description"]
            )
        self.stdout.write(self.style.SUCCESS("HomePage slides loaded."))

        # 2. Doctors Data
        fallbackDoctors = [
            {
                "name": "Dr. Sujeet Parajuli",
                "highest_degree": "BDS",
                "years_of_experience": 1,
                "nmc_number": "37983",
                "slug": "dr-sujeet-parajuli",
                "details": "Dr. Sujeet Parajuli is a Dental Surgeon who completed his Bachelor of Dental Surgery (BDS) in 2025... As the Founder of the clinic, he is dedicated.",
            },
            {
                "name": "Dr. Bhuwan Niroula",
                "highest_degree": "MDS, Prosthodontist, Maxillofacial prosthetics and implant dentistry",
                "years_of_experience": 1,
                "nmc_number": "15047",
                "slug": "dr-bhuwan-niroula",
                "details": "Dr. Bhuwan Niroula completed BDS... patients benefit from specialized prosthodontic expertise while receiving comprehensive dental care under one roof.",
            },
            {
                "name": "Dr. Subodh Khadka",
                "highest_degree": "MDS , Orthodontist ",
                "years_of_experience": 1,
                "nmc_number": "17292",
                "slug": "dr-subodh-khadka",
                "details": "Dr. Subodh completed BDS from BPKISH Dharan in 2014... He believes in personalized treatment planning to achieve a confident smile and balanced facial aesthetics.",
            },
            {
                "name": "Dr. Kamal Pandey",
                "highest_degree": "MDS, Periodontology & Oral Implantology",
                "years_of_experience": 5,
                "nmc_number": "20721",
                "slug": "dr-kamal-pandey",
                "details": "Dr. Kamal Pandey has completed BDS from Kathmandu University School of Medical Science (KUSMS)... He also manages peri-implant diseases and focuses on restoring oral health, function, and aesthetics through evidence-based periodontal care.",
            },
            {
                "name": "Dr. Siddhartha Sharma",
                "highest_degree": "MDS, Oral & Maxillofacial Surgeon",
                "years_of_experience": 8,
                "nmc_number": "20003",
                "slug": "dr-siddhartha-sharma",
                "details": "Dr. Siddhartha Sharma completed BDS from BPKIHS Dharan in 2017... Dr. Sharma is also experienced in facial trauma management, jaw fracture stabilization, TMJ-related procedures, and minor orthognathic interventions.",
            },
            {
                "name": "Dr. Aliza Khadka",
                "highest_degree": "BDS, Dental Surgeon",
                "years_of_experience": 1,
                "nmc_number": "39721",
                "slug": "dr-aliza-khadka",
                "details": "Dr. Aliza Khadka is a dedicated dental surgeon providing quality dental care to patients at Hridaya Dental Clinic.",
            },
            {
                "name": "Dr. Pragya Pokhrel",
                "highest_degree": "BDS, Dental Surgeon",
                "years_of_experience": 1,
                "nmc_number": "37764",
                "slug": "dr-pragya-pokhrel",
                "details": "Dr. Pragya Pokhrel has completed BDS from Nepal Medical College, Kathmandu University in 2025... She emphasizes preventive dentistry, patient education, and comfortable treatment delivery.",
            },
        ]
        Doctor.objects.all().delete()
        for doc in fallbackDoctors:
            Doctor.objects.create(**doc)
        self.stdout.write(self.style.SUCCESS("Doctors loaded."))

        # 3. Testimonials
        fallbackTestimonials = [
            {
                "name": "Dr. Siddhartha Sharma",
                "designation": "MDS, Oral & Maxillofacial Surgeon",
                "message": "At Hridaya, we blend precision surgery with genuine compassion — every patient leaves healthier and happier.",
            },
            {
                "name": "Dr. Kamal Pandey",
                "designation": "MDS, Periodontology & Oral Implantology",
                "message": "Our commitment to evidence-based care ensures every smile we restore is built on a foundation of trust and expertise.",
            },
            {
                "name": "Dr. Sujeet Parajuli",
                "designation": "BDS, Founder",
                "message": "We built Hridaya with one belief — ethical, patient-first dentistry can truly change lives, one smile at a time.",
            },
        ]
        Testimonial.objects.all().delete()
        for tm in fallbackTestimonials:
            t = Testimonial.objects.create(**tm)
            t.is_approved = True
            t.save()
        self.stdout.write(self.style.SUCCESS("Testimonials loaded."))

        # 4. Services
        Service.objects.all().delete()

        gen_dentistry = Service.objects.create(name="General Dentistry", slug="general-dentistry", description="Comprehensive general dental care for the whole family")
        spec_dentistry = Service.objects.create(name="Specialized Dentistry", slug="specialized-dentistry", description="Advanced specialist dental treatments")
        pharmacy = Service.objects.create(
            name="Pharmacy", slug="pharmacy", 
            description="At Sushi Pharmacy, we are committed to making your dental care experience more convenient by providing a complete pharmacy facility...",
            extra_info=""
        )

        sub_services_data = [
            ("Dental Checkup & Consultation", "dental-checkup-consultation", "Thorough oral examination, diagnosis, and personalized treatment planning for optimal dental health.", "<h3>What's Included</h3><p>Our comprehensive dental checkup includes a thorough examination of your teeth, gums, and oral tissues. We use digital X-rays for accurate diagnosis and create a personalized treatment plan.</p><ul><li>Complete oral examination</li><li>Digital X-rays</li><li>Oral cancer screening</li><li>Treatment plan discussion</li><li>Preventive care advice</li></ul>", gen_dentistry),
            ("Scaling & Polishing", "scaling-polishing", "Professional teeth cleaning to remove plaque, tartar, and surface stains for healthier gums.", "<h3>About the Procedure</h3><p>Professional scaling removes hardened plaque, stain and calculus from tooth surfaces and below the gumline, while polishing smoothens the tooth surface.</p><ul><li>Prevents gum disease</li><li>Removes tartar and stains</li><li>Freshens breath</li><li>Promotes overall oral health</li></ul>", gen_dentistry),
            ("Tooth Extraction", "tooth-extraction", "Safe and painless simple and surgical tooth extractions with proper post-operative care.", "<h3>Types of Extraction</h3><p>We perform both simple and surgical extractions using modern techniques for minimal discomfort and faster recovery.</p><ul><li>Simple extraction</li><li>Surgical extraction</li><li>Wisdom tooth removal</li><li>Post-operative care guidance</li></ul>", gen_dentistry),
            ("Root Canal Treatment (RCT)", "root-canal-treatment", "Advanced endodontic treatment to save infected teeth and relieve pain effectively.", "<h3>The Procedure</h3><p>Root canal treatment saves a severely infected tooth by removing infected pulp, cleaning the canals, and sealing them.</p><ul><li>Pain-free under local anesthesia</li><li>Single or multi-visit treatment</li><li>Re-root canal procedures available</li><li>Crown recommendation for protection</li></ul>", gen_dentistry),
            ("Dental Fillings & Restorations", "dental-fillings-restorations", "Tooth-colored composite fillings and restorations for cavities and damaged teeth.", "<h3>Restoration Options</h3><p>We use high-quality, tooth-colored materials to restore teeth affected by decay or damage.</p><ul><li>Composite fillings</li><li>Glass ionomer restorations</li><li>Anterior aesthetic restorations</li><li>Inlays and onlays</li></ul>", gen_dentistry),
            ("Teeth Whitening", "teeth-whitening", "Professional teeth whitening treatments for a brighter, more confident smile.", "<h3>Whitening Options</h3><p>Our professional whitening treatments are safe, effective, and deliver noticeable results.</p><ul><li>In-office professional whitening</li><li>Customized treatment</li><li>Safe for enamel</li><li>Long-lasting results</li></ul>", gen_dentistry),
            
            ("Orthodontics (Braces & Aligners)", "orthodontics", "Metal braces, ceramic braces, and clear aligners for teeth alignment and jaw correction.", "<h3>Treatment Options</h3><p>Comprehensive solutions for misaligned teeth and jaw discrepancies for all ages.</p>...", spec_dentistry),
            ("Dental Implants", "dental-implants", "Permanent tooth replacement with titanium implants for natural-looking, functional results.", "<h3>Implant Solutions</h3><p>Dental implants are the gold standard for replacing missing teeth.</p><ul><li>Single tooth implants</li><li>Multiple teeth replacement</li><li>Bone grafting</li><li>Sinus lift procedures</li><li>Implant-supported dentures</li></ul>", spec_dentistry),
            ("Periodontal Treatment", "periodontal-treatment", "Treatment of gum diseases from mild gingivitis to advanced periodontitis.", "<h3>Gum and Bone Care Services</h3><p>Specialized treatment for all stages of gum disease and aesthetic gum procedures.</p><ul><li>Scaling and root planing</li><li>Gingivectomy & gingivoplasty</li><li>Gummy smile correction</li><li>Flap surgeries</li><li>GTR & GBR techniques</li><li>Gingival depigmentation</li><li>Splinting</li></ul>", spec_dentistry),
            ("Oral Surgery", "oral-surgery", "Minor and major oral surgical procedures including impacted teeth, cysts, and trauma management.", "<h3>Surgical Expertise</h3><p>Full spectrum of oral surgical procedures with precision and expertise.</p><ul><li>Impacted third molar surgery</li><li>Cyst and tumor removal</li><li>Frenectomy</li><li>Facial trauma management</li><li>TMJ procedures</li></ul>", spec_dentistry),
            ("Pediatric Dentistry", "pediatric-dentistry", "Gentle dental care for children including preventive treatments and habit counseling.", "<h3>Child-Friendly Care</h3><p>Gentle, compassionate dental care designed for children.</p><ul><li>Child tooth extractions</li><li>Restorations</li><li>Pulpotomy & pulpectomy</li><li>Fluoride treatments</li><li>Habit counseling</li><li>Early preventive and interceptive dentistry</li><li>Functional and Non-functional appliances</li></ul>", spec_dentistry),
            ("Emergency Dental Care", "emergency-dental-care", "Urgent dental treatment for toothaches, trauma, infections, and dental emergencies.", "<h3>Emergency Services</h3><p>Immediate attention for dental emergencies.</p><ul><li>Severe toothache relief</li><li>Dental trauma management</li><li>Abscess drainage</li><li>Broken tooth repair</li><li>Same-day appointments</li></ul>", spec_dentistry),
            ("Prosthodontic Treatments", "prosthodontic-treatments", "Advanced solutions designed to restore missing or damaged teeth, improving chewing function, comfort, and smile aesthetics.", "<h3>Treatment Options</h3><p>Specialized dental procedures </p><ul><li>Full Mouth Rehabilitation (comprehensive restoration for severely worn or multiple missing teeth)</li><li>Dental trauma management</li><li>Dental Crowns and Bridges (fixed solutions to restore damaged or missing teeth)</li><li>Implant-Supported Prosthesis (implant crowns, bridges, and implant-supported dentures)</li><li>Complete Dentures (for patients with complete tooth loss)</li><li>Removable Partial Dentures (replacement for several missing teeth)</li><li>Veneers and Aesthetic Smile Restoration (cosmetic improvement of front teeth)</li><li>Post and Core Restorations (strengthening root canal treated teeth before crown placement)</li><li>Occlusal Rehabilitation (bite correction for worn teeth, jaw discomfort, and functional restoration)</li><li>Custom Night Guards / Mouth Guards (protection against teeth grinding, clenching, and sports injuries)</li></ul>", spec_dentistry),
        ]

        for num, (name, slug, desc, extra, parent) in enumerate(sub_services_data):
            Service.objects.create(name=name, slug=slug, description=desc, extra_info=extra, parent=parent)

        self.stdout.write(self.style.SUCCESS("Services loaded."))
        self.stdout.write(self.style.SUCCESS("Seed data loaded successfully!"))
