from django import forms
from .models import UserInfo


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            "name",
            "dob",
            "email",
            "phone",
            "address",
            "roll",
            "class_name",
            "year",
            "previous_school",
            "documents",
            "parent_name",
            "parent_phone",
            "parent_email",
            "terms",
        ]
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date"}),
            "class_name": forms.Select(
                choices=[
                    ("", "Select Grade"),
                    ("Grade 1", "Grade 1"),
                    ("Grade 2", "Grade 2"),
                    ("Grade 3", "Grade 3"),
                    ("Grade 4", "Grade 4"),
                    ("Grade 5", "Grade 5"),
                    ("Grade 6", "Grade 6"),
                    ("Grade 7", "Grade 7"),
                    ("Grade 8", "Grade 8"),
                    ("Grade 9", "Grade 9"),
                    ("Grade 10", "Grade 10"),
                    ("Grade 11", "Grade 11"),
                    ("Grade 12", "Grade 12"),
                ]
            ),
        }
