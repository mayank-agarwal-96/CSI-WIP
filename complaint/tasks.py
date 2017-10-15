from celery.decorators import task
from complaint.models import Profile
from django.core.mail import send_mail


@task(name="find_and_send")
def add(complaint):
    dept_map = {
        "education": "EDC",
        "cosha": "CSH",
        "hostel": "HST",
        "general": "GEN"
    }

    department = dept_map[complaint.department]
    users = Profile.objects.filter(department=department)
    recepients = [str(name.user.email) for name in users]
    print recepients
    subject = "New Complaint Posted in " + complaint.department
    msg = complaint.data
    frm = "LNMIIT Complaints"
    send_mail(subject, msg, frm, recepients)