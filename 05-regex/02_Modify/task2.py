import re

#reg = re.compile(r"((?:Dr\.|Prof\.|Prince)?\s?(?:Dr\.\s?)*)?([A-Z][a-z]+(?: [A-Z][a-z]+)*)?,? (?:[A-Z](?:[a-z]*\.? )?)*([A-Z][a-z]+)(?:,? (?:PhD|MSc|KG|KT|PC|ADC|Duke of Manchester)([A-Za-z]+))*")

reg = re.compile("([A-Z][a-z\.]+)(( |, )([A-Z]*([a-z\.A-Z]+)?)){0,10}(?:( |, )([A-Z]*([a-z]+)?)){0,10}")

m = reg.match("Uwe Meier")
print(m)
m = reg.match("Prof. Dr. Chris C Schmidt")
print(m)
m = reg.match("Hanna J Gruber, PhD")
print(m)
m = reg.match("Hanna J. Gruber, PhD")
print(m)
m = reg.match("Hanna Jana Gruber, PhD, MSc")
print(m)
m = reg.match("Dr. Uwe Meier, MSc")
print(m)
m = reg.match("Dr. Alfred Nobel, PhD, PhD, PhD, MSc")
print(m)
m = reg.match("Dr. Dr. Dr. Theodore Hesburgh, PhD, PhD, PhD, MSc")
print(m)
m = reg.match("Albert KD Klein, PhD, PhD, PhD, MSc")
print(m)
m = reg.match("Prince William, Duke of Manchester, KG, KT, PC, ADC")
print(m)
