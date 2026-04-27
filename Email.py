import smtplib


class Email():
    def sendemail(self,name,email):
        companyEmail="kya re bhik mange apni khud ki Email daal"
        password="password kya dekh raha hai khud ka bana"


        s = smtplib.SMTP('smtp.gmail.com', 587)
      
        s.starttls()
        
        s.login(companyEmail, password)
      
        message =  f"""Subject: Welcome to MediConnect

                    Hi {name.upper()},

                    Thank you for registering on MediConnect!

                    You can now:
                    -> Browse hospitals
                    -> Explore doctors
                    -> Get better healthcare information

                    We're glad to have you with us.

                    Best regards,  
                    MediConnect Team
                    """
    
        s.sendmail(companyEmail, email, message)
    
        s.quit()