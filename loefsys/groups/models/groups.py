from django.db import models
from rest_framework.exceptions import ValidationError

from groups.models.membergroup import MemberGroup, ActiveMemberGroupManager

from django.utils.translation import gettext_lazy as _

from utils.snippets import overlaps


class Committee(MemberGroup):
    """Describes a committee, which is a type of MemberGroup."""

    objects = models.Manager()
    active_objects = ActiveMemberGroupManager()

    mandatory = models.BooleanField()

    # def get_absolute_url(self):
    #     return reverse("activemembers:committee", args=[str(self.pk)])

    class Meta:
        verbose_name = _("committee")
        verbose_name_plural = _("committees")
        # ordering is done in the manager, to sort on a translated field


class Board(MemberGroup):
    """Describes a board, which is a type of MemberGroup."""

    class Meta:
        verbose_name = _("board")
        verbose_name_plural = _("boards")
        ordering = ["-since"]

    def save(self, **kwargs):
        self.active = True
        super().save(**kwargs)

    # def get_absolute_url(self):
    #     return reverse(
    #         "activemembers:board", args=[str(self.since.year), str(self.until.year)]
    #     )

    def validate_unique(self, **kwargs):
        super().validate_unique(**kwargs)
        boards = Board.objects.all()
        if self.since is not None:
            if overlaps(self, boards, can_equal=False):
                raise ValidationError(
                    {
                        "since": _("A board already exists for those years"),
                        "until": _("A board already exists for those years"),
                    }
                )
