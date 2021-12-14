from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, redirect
from django.urls import reverse


class LoginCheckMiddleWare(MiddlewareMixin):
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        # print(modulename)
        user = request.user

        #Check whether the user is logged in or not
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "student_management_app.HodViews":
                    pass
                elif modulename == "student_management_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("admin_profile")
            
            elif user.user_type == "2":
                if modulename == "student_management_app.StaffViews":
                    pass
                elif modulename == "student_management_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("staff_profile")
            
            elif user.user_type == "3":
                if modulename == "student_management_app.StudentViews":
                    pass
                elif modulename == "student_management_app.views" or modulename == "django.views.static":
                    pass
                else:
                    return redirect("student_profile")

            else:
                return redirect("home")

        else:
            if request.path == reverse("login") or request.path == reverse("doLogin"):
                pass
            elif request.path == reverse("home") or request.path == reverse("home"):
                pass
            elif request.path == reverse("about") or request.path == reverse("about"):
                pass
            elif request.path == reverse("contact") or request.path == reverse("contact"):
                pass
            elif request.path == reverse("doContact") or request.path == reverse("doContact"):
                pass                
            else:
                return redirect("home")
