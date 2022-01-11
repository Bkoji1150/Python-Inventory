#!/usr/bin/env python3

"""
Superscript and subscript research finding
https://www.geeksforgeeks.org/how-to-print-superscript-and-subscript-in-python/
"""
from openpyxl import Workbook
# function to convert to superscript


def get_super(x):
    try:
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
        super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
        res = x.maketrans(''.join(normal), ''.join(super_s))
        return x.translate(res)
    except Exception as e:
        print(e)

#
# # display superscipt
# print(get_super('GeeksforGeeks')) #ᴳᵉᵉᵏˢᶠᵒʳᴳᵉᵉᵏˢ
# # function to convert to subscript
# def get_sub(x):
# 	normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
# 	sub_s = "ₐ₈CDₑբGₕᵢⱼₖₗₘₙₒₚQᵣₛₜᵤᵥwₓᵧZₐ♭꜀ᑯₑբ₉ₕᵢⱼₖₗₘₙₒₚ૧ᵣₛₜᵤᵥwₓᵧ₂₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎"
# 	res = x.maketrans(''.join(normal), ''.join(sub_s))
# 	return x.translate(res)
#
# # display subscript
# print('H{}SO{}'.format(get_sub('2'),get_sub('4'))) #H₂SO₄
# print(get_sub('a'))
# # subscript
# print(u'H\u2082SO\u2084')  # H₂SO₄
# val1 = u'H\u2082SO\u2084'
# # superscript
# print("x\u00b2 + y\u00b2 = 2")  # x² + y² = 2
# val2 = "x\u00b2 + y\u00b2 = 2"
# val3 = get_super('a')
# val4 = '{}For the a  measure.'.format((get_super('a')))
# val5 = '{}To Start with b measure.'.format((get_super('b')))
# val6 = '{}For the a  measure.'.format((get_super('c')))
# val7 = '{}To suStart with b meare.'.format((get_super('d')))
#
# val8 = '\033[1m' + 'Bolded for the a  measure bolded ended' + '\033[0m' + 'Un bolded text following the bolded text'
#
# val9 = '\033[1m' + 'For the a  measure' + '\033[0m'
# print(val4)
# print(val8)
# print(val9)
# if __name__ == "__main__":
# 	# Create a workbook and sheets
#     filename = "SpecialChars.xlsx"
#     wb = Workbook()
#     ws1 = wb["Sheet"]
#     # Create Special data a list of lists
#     special_data = [ ["One",  val1, val2],\
#                   ["Two", val3, val4],\
#                   ["Three", val5, val6],
#                   ["Four", val1, val3] ]
#     # add column headings
#     ws1.append( ["Superscript", "Type1", "Type2"] )
#     for row in special_data:
#         ws1.append(row)
#     wb.save(filename)