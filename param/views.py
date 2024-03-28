import base64 as b64
import hashlib
from urllib.parse import quote, unquote
import json
from datetime import datetime, timezone

from django.shortcuts import render


# Create your views here.
def index(request):
    pass


def base64(request):
    context = {
        "result": "",
        "input_text": "",
        "operation": "encode",
        "error": "",
    }

    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        operation = request.POST.get("operation", "")
        context["input_text"] = input_text
        context["operation"] = operation

        if input_text:
            try:
                if operation == "encode":
                    result = b64.b64encode(input_text.encode()).decode()
                else:
                    result = b64.b64decode(input_text).decode()
                context["result"] = result
            except Exception as e:
                context["error"] = f"{str(e)}"

    return render(request, "param/base64.html", context)


def hash_md5(request):
    context = {
        "result": "",
        "input_text": "",
        "error": "",
    }

    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        context["input_text"] = input_text

        try:
            result = hashlib.md5(input_text.encode()).hexdigest()
            context["result"] = result
        except Exception as e:
            context["error"] = f"{str(e)}"
    return render(request, "param/md5.html", context)


def url_encoding(request):
    context = {
        "result": "",
        "input_text": "",
        "operation": "encode",
        "error": "",
    }

    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        operation = request.POST.get("operation", "")
        context["input_text"] = input_text
        context["operation"] = operation

        if input_text:
            try:
                if operation == "encode":
                    result = quote(input_text)
                else:
                    result = unquote(input_text)
                context["result"] = result
            except Exception as e:
                context["error"] = f"{str(e)}"

    return render(request, "param/url.html", context)


def json_formatter(request):
    context = {
        "result": "",
        "input_text": "",
        "error": "",
    }

    if request.method == "POST":
        input_text = request.POST.get("input_text", "")
        context["input_text"] = input_text

        try:
            result = json.loads(input_text)
            context["result"] = json.dumps(result, indent=4, sort_keys=True)
        except json.JSONDecodeError as e:
            context["error"] = f"{str(e)}"

    return render(request, "param/json.html", context)


def timestamp_converter(request):
    context = {
        "result": "",
        "input_value": "",
        "operation": "to_human",
        "error": "",
    }

    if request.method == "POST":
        input_value = request.POST.get("input_value", "")
        operation = request.POST.get("operation", "to_human")
        context["input_value"] = input_value
        context["operation"] = operation

        if input_value:
            try:
                if operation == "to_human":
                    timestamp = int(input_value)
                    converted_time = datetime.fromtimestamp(timestamp, tz=timezone.utc)
                    context["result"] = converted_time.strftime("%Y-%m-%d %H:%M:%S %Z")
                else:
                    date_time_obj = datetime.strptime(
                        input_value, "%Y-%m-%d %H:%M:%S"
                    ).replace(tzinfo=timezone.utc)
                    context["result"] = str(int(date_time_obj.timestamp()))
            except ValueError as e:
                context["error"] = f"{str(e)}"
    return render(request, "param/timestamp.html", context)
