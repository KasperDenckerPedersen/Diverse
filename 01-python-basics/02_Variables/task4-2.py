# Assign your first and your last name to 2 separate variables with suitable names.
# Output your full name as well as your initials using one print statement.

firstName = "Kasper"
middleName = "Dencker"
lastName = "Pedersen"
initials = firstName[:1] + middleName[:1] + lastName[:1]

print(f"My full name is {firstName} {middleName} {lastName} and my initials is {initials}")
