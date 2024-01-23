from django.shortcuts import render
from django.contrib import messages

def home(request):
	
	lang_list=['c', 'clike', 'csharp', 'cshtml', 'css', 'css-extras', 'csv', 'dart', 'django', 'go', 'html', 'java', 'javascript', 'js-templates', 'markdown', 'markup', 'markup-templating', 'mongodb', 'perl', 'php', 'plsql', 'powerquery', 'powershell', 'python', 'r', 'ruby', 'rust', 'sql', 'swift', 'typescript', 'typoscript', 'yaml']

	if request.method == "POST":
		code = request.POST['code']
		lang = request.POST['lang']
		return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})

		if lang == "Select Programming Languages":
			messages.success(request, "Hey you forgot to PICK A Programming Languages...")
			return render(request, 'home.html', {'lang_list':lang_list, 'code':code, 'lang':lang})

	return render(request, 'home.html', {'lang_list':lang_list})
