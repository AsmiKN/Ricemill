from django.db import models

# Create your models here.
class tbl_team(models.Model):
   team_name=models.CharField(max_length=50)

class tbl_playercategory(models.Model):
   playercategory_name=models.CharField(max_length=50)

class tbl_playerdetails(models.Model):
   playerdetails_name=models.CharField(max_length=50)
   playerdetails_dob=models.CharField(max_length=50)
   team= models.ForeignKey(tbl_team, on_delete=models.CASCADE)
   playercategory= models.ForeignKey(tbl_playercategory, on_delete=models.CASCADE)
   playerdetails_photo = models.FileField(upload_to='Assets/UserPhoto/')
   playerdetails_status = models.IntegerField(default="0")


class tbl_matchschedule(models.Model):
   match_name=models.CharField(max_length=50)
   match_todate=models.CharField(max_length=50)
   match_fromdate=models.CharField(max_length=50)
   match_venue=models.CharField(max_length=50)


class tbl_playerxi(models.Model):
   playerdetails= models.ForeignKey(tbl_playerdetails, on_delete=models.CASCADE)    
   matchschedule= models.ForeignKey(tbl_matchschedule, on_delete=models.CASCADE)
