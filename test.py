import sys
import os
import argparse
import urllib2

path = ''
index_template = 'index.html'


def check_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)
    global path
    path = d
    return

def create(n):
    #create directory structure
    global path
    proj_path = path+'/'+n 
    if not os.path.exists(proj_path):
        os.makedirs(proj_path)
    os.makedirs(proj_path+'/app/shared')
    os.makedirs(proj_path+'/app/components')
    os.makedirs(proj_path+'/assets/img')
    os.makedirs(proj_path+'/assets/css')
    os.makedirs(proj_path+'/assets/js')
    os.makedirs(proj_path+'/assets/libs/angular')
    os.makedirs(proj_path+'/assets/libs/bootstrap')

    #index
    o = open(proj_path+'/index.html', 'w').writelines(l for l in open(index_template).readlines())

    #angular 
    f = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular.min.js')
    open(proj_path+'/assets/libs/angular/angular.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://cdnjs.cloudflare.com/ajax/libs/angular-ui-router/0.2.8/angular-ui-router.min.js')
    open(proj_path+'/assets/libs/angular/angular-route.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular-resource.min.js')
    open(proj_path+'/assets/libs/angular/angular-resource.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular-animate.min.js')
    open(proj_path+'/assets/libs/angular/angular-animate.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular-aria.min.js')
    open(proj_path+'/assets/libs/angular/angular-aria.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular-messages.min.js')
    open(proj_path+'/assets/libs/angular/angular-messages.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://ajax.googleapis.com/ajax/libs/angular_material/1.1.0/angular-material.min.js')
    open(proj_path+'/assets/libs/angular/angular-material.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('https://cdnjs.cloudflare.com/ajax/libs/angular-material-icons/0.7.1/angular-material-icons.min.js')
    open(proj_path+'/assets/libs/angular/angular-material-icons.min.js', 'w').writelines(f.read())
    f = urllib2.urlopen('http://ajax.googleapis.com/ajax/libs/angular_material/1.1.0/angular-material.min.css')
    open(proj_path+'/assets/libs/angular/angular-material.min.css', 'w').writelines(f.read())
    f = urllib2.urlopen('https://fonts.googleapis.com/icon?family=Material+Icons')
    open(proj_path+'/assets/libs/angular/angular-material-icons.css', 'w').writelines(f.read())

    #bootstrap
    f = urllib2.urlopen('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css')
    open(proj_path+'/assets/libs/bootstrap/bootstrap.min.css', 'w').writelines(f.read())
    f = urllib2.urlopen('https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css')
    open(proj_path+'/assets/libs/bootstrap/bootstrap-theme.min.css', 'w').writelines(f.read())
    

    
parser = argparse.ArgumentParser(description='asdfg')
parser.add_argument('-d', help='directory', type=check_dir, nargs=1)
parser.add_argument('-n', help='asf', type=create, nargs=1)
args = parser.parse_args()


