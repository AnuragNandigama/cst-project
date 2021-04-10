from django.test import TestCase
from jobs.models import Job, Profile, StudentDetails
from jobs.forms import StudentDetailsForm


# Create your tests here.
class JobTest(TestCase):
    def create_jobs(self, image='images\codejpeg.jpeg', summary="This is my first job!"):
        return Job.objects.create(image=image, summary=summary)
    
    def test_job_creation(self):
        job = self.create_jobs()
        self.assertTrue(isinstance(job, Job))
        self.assertEqual(job.__str__(), job.summary)
    

class ProfileTest(TestCase):
    def create_profile(self, profile='Local'):
        return Profile.objects.create(profile=profile)
    
    def test_profile_creation(self):
        prof = self.create_profile()
        self.assertTrue(isinstance(prof, Profile))
        self.assertEqual(prof.__str__(), prof.profile)
        
class StudentDetailsTest(TestCase):
    def create_profile(self, profile='International'):
        return Profile.objects.create(profile=profile)
    
    def create_student_details(self, user_name='Anurag', user_college='MCIT', user_profile='International'):
        return StudentDetails.objects.create(user_name=user_name, user_college=user_college, user_profile=self.create_profile())
    
    def test_student_details_creation(self):
        student = self.create_student_details()
        self.assertTrue(isinstance(student, StudentDetails))
        self.assertEqual(student.__str__(), student.user_name)
