from django.db import models

class Inventory(models.Model):
    instance_name = models.CharField(max_length=100)
    host_ip = models.GenericIPAddressField()
    user = models.CharField(max_length=100)
    ssh_key_path = models.CharField(max_length=200)
    python_interpreter = models.CharField(max_length=200)

    def __str__(self):
        return self.instance_name  # Updated from self.name to self.instance_name

