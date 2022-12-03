from django.urls import path
# from .views import RegView,ViewEmp,DeleteEmp,EditEmp,DeptView,DepRet,DepDelete,DeptEdit
from .views import *

urlpatterns=[
    path('reg/',RegView.as_view(),name="reg"),
    path('vemp/',ViewEmp.as_view(),name="vemp"),
    path('delemp/<int:id>',DeleteEmp.as_view(),name="delemp"),
    path('editemp/<int:id>',EditEmp.as_view(),name="editemp"),
    path('dept/',DeptView.as_view(),name="dept"),
    path('depr/',DepRet.as_view(),name="depret"),
    path('deptdel/<int:did>',DepDelete.as_view(),name="deptdel"),
    path('deptedit/<int:did>',DeptEdit.as_view(),name="deptedit"),
    path('addman/',ManagerReg.as_view(),name="addman"),
    path('viewman/',ManagerList.as_view(),name="viewman"),
    path('delmang/<int:mid>',DelMang.as_view(),name="delmang"),
    path('editman/<int:mid>',EditMang.as_view(),name="editman")

]
