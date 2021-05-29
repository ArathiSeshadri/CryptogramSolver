# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  ╔═╗╦═╗╦ ╦╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗                       #
#  ║  ╠╦╝╚╦╝╠═╝ ║ ║ ║║ ╦╠╦╝╠═╣║║║                       #
#  ╚═╝╩╚═ ╩ ╩   ╩ ╚═╝╚═╝╩╚═╩ ╩╩ ╩                       #
#  ╔═╗╔═╗╦ ╦  ╦╔═╗╦═╗                                   #
#  ╚═╗║ ║║ ╚╗╔╝║╣ ╠╦╝                                   #
#  ╚═╝╚═╝╩═╝╚╝ ╚═╝╩╚═                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                       #
# Licensed under the GNU GENERAL PUBLIC LICENSE v3.0    #
#                                                       #
# 29 May 2021                                           #
#                                                       #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# APPROACH:
#
# 1. ACCEPT THE CIPHER
# 2. ACCEPT THE CLUE
# 3. DUPLICATE THE CIPHER
# 4. PARSE THE CIPHER AT SPACES OR PUNCTUATION INTO AN ARRAY
# 5. ORDER ARRAY ELEMENTS BY LENGTH
# 6. COMPARE ORIGINAL ARRAY AND ORDERED ARRY AND BUILD A DICTIONARY TO REMEMBER ORIGINAL ORDERING
# 7. DUPLICATE THE ARRAY (?)
# 8. SUBSTITUTE THE CLUE INTO ALL ARRAY ELEMENTS
# 9. COMPARE WITH DICTIONARY TO FIND WORD MATCHES IN ASCENSION OF ELEMENT LENGTH
# 10. RESTART AT ARRAY 0 FOR EVERY FAILED MATCH ENCOUNTERED
# 11. ONCE ALL ARRAY ELEMENTS HAVE BEEN MATCHED COMPARE ELEMENTS TO THE DICTIONARY AND RE-ORDER ARRAY
# 12. CONCATENATE ARRAY INTO A PROPER SENTENCE
#
# ISSUES:
#
# 1.
# 2.
# 3.
#