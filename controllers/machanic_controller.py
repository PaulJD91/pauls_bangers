from flask import Flask, Blueprint, render_template, redirect, request
from app import db
from models.mechanic import Mechanic
from models.car import Car