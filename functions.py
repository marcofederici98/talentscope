def ans_gen(ans):
    code = '<form>'
    for i in ans:
        code += f"""<input class="form-check-input" type="radio">
    <label class="form-check-label">
        {i}
      </label><br>"""
    code +='</form>'
    return code

