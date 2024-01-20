from django.shortcuts import render
from .forms import CipherForm
from .utils.monoalphabetic import MonoalphabeticCipher
from .utils.caesar import caesar, caesar_decrypt
from .utils.railfence import encrypt_rail_fence, decrypt_rail_fence
from .utils.vignere import vignere, vignere_decrypt


def home(request):
    result_text = None

    if request.method == 'POST':
        form = CipherForm(request.POST)
        if form.is_valid():
            input_text = form.cleaned_data['input_text']
            algorithm = form.cleaned_data['algorithm']
            key = form.cleaned_data['key']
            operation = form.cleaned_data['operation']

            if algorithm == 'monoalphabetic':
                cipher = MonoalphabeticCipher(key="QWERTYUIOPASDFGHJKLZXCVBNM")
                if operation == 'encrypt':
                    result_text = cipher.encrypt(input_text)
                elif operation == 'decrypt':
                    result_text = cipher.decrypt(input_text)
            elif algorithm == 'caesar':
                result_text = caesar(input_text, shift=int(key) if key else 0) if operation == 'encrypt' else caesar_decrypt(input_text, shift=int(key) if key else 0)
            elif algorithm == 'railfence':
                if operation == 'encrypt':
                    result_text = encrypt_rail_fence(input_text, key=int(key) if key else 3)
                elif operation == 'decrypt':
                    result_text = decrypt_rail_fence(input_text, key=int(key) if key else 3)
            elif algorithm == 'vignere':
                result_text = vignere(input_text, key=key) if operation == 'encrypt' else vignere_decrypt(input_text, key=key)
            else:
                result_text = "Invalid algorithm"

    else:
        form = CipherForm()

    return render(request, 'cipher/home.html', {'form': form, 'result_text': result_text})
