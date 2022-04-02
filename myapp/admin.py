# Register your models here.
from django.contrib import admin
from  .models import Topic, Course, Student, Order, Review, CourseAdmin, OrderAdmin

class CourseInline(admin.TabularInline):
    model = Course
    fields = [('title', 'topic'), ('price', 'num_reviews', 'for_everyone')]
    list_display = ('title', 'topic', 'price')

class TopicAdmin(admin.ModelAdmin):
    fields = [('name','length')]
    list_display = ('name','length')
    inlines = [CourseInline]

class StudentAdmin(admin.ModelAdmin):
    fields = [('first_name', 'last_name','password','email','level','registered_courses')]
    list_display = ('first_name', 'last_name','password','email','level')

# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Review)
