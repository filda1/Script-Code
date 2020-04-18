# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager, models.Manager):

	def _create_user(self, username, email, password, is_staff,
			is_superuser, **extra_fields):
		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')
		user = self.model(username=username, email=email, is_active=True,
				is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False,
			False,**extra_fields)

	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True,
			True, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    avatar = models.URLField(blank = True)
    nivel_user = models.CharField(max_length=1)
    #titulo = models.ManyToManyField(Titulo,blank=True)
    #asesorado = models.ManyToManyField(Tesista,blank=True)
    #grado = models.ManyToManyField(Grado)
    objects = UserManager()
    is_colaborador=models.BooleanField(default=True)
    is_gerente=models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.username

	def gerente(self):
		if self.nivel_user == 1:
			self.is_gerente = True
		return self.is_gerente

	def colaborador(self):
		if self.nivel_user == 0:
			self.is_colaborador = True
		return self.is_colaborador
