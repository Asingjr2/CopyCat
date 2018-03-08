from abc import ABC, abstractmethod
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class ModeratorRequiredMixin(LoginRequiredMixin, ABC):
    @abstractmethod
    def get_forum(self):
        pass

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        forum = self.get_forum()
        if not forum.moderators.filter(username=user.username).exists():
            return redirect(forum.get_absolute_url())

        return super().dispatch(request, *args, **kwargs)