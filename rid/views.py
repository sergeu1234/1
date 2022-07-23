from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']  # here message-name comes from contact.html file's input type name
        message_email = request.POST['message-email']
        message = request.POST['message']

        ### Send an Email Start ###
        send_mail(
            message_name, # subject
            message, # message
            message_email, # from email
            ['omarfaruk2468@gmail.com','mehedibinhafiz@gmail.com',],