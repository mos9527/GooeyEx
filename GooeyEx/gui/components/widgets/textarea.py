import os
import wx  # type: ignore
from functools import reduce

from GooeyEx.gui.components.widgets.core.text_input import MultilineTextInput
from GooeyEx.gui.components.widgets.textfield import TextField
from GooeyEx.gui.components.widgets.bases import TextContainer
from GooeyEx.gui import formatters
from GooeyEx.python_bindings import types as t
from GooeyEx.python_bindings.types import FormField


class Textarea(TextContainer):

    def getWidget(self, parent, *args, **options):
        widgetHeight = self._options.get("height", -1)
        return wx.TextCtrl(
            parent=parent, size=(-1, widgetHeight), style=self.getModifiers()
        )

    def getModifiers(self):
        readonly = (
            wx.TE_READONLY
            if self._options.get("readonly", False)
            # using TE_MUTLI as a safe OR-able no-op value
            else wx.TE_MULTILINE
        )
        return reduce(lambda acc, val: acc | val, [wx.TE_MULTILINE, readonly])

    def getWidgetValue(self):
        return self.widget.GetValue()

    def setValue(self, value):
        self.widget.Clear()
        self.widget.AppendText(str(value))
        self.widget.SetInsertionPoint(0)

    def formatOutput(self, metatdata, value: str):
        return formatters.general(metatdata, value.replace("\n", os.linesep))

    def syncUiState(self, state: FormField):
        self.setValue(state["value"])  # type: ignore
        self.error.SetLabel(state["error"] or "")
        self.error.Show(state["error"] is not None and state["error"] is not "")

    def getUiState(self) -> t.FormField:
        return t.TextField(
            id=self._id,
            type=self.widgetInfo["type"],
            value=self.getWidgetValue(),
            placeholder=self.widget.GetHint(),
            error=self.error.GetLabel().replace("\n", " "),
            enabled=self.IsEnabled(),
            visible=self.IsShown(),
        )
