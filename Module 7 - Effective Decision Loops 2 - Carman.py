START
    # DECLARATIONS
    num yearsRemaining
    num annualSavings
    num INTEREST = 1.03
    num EXPENSES = 60000
    num savingBalance = 0
    num MAX_RETIRE = 30
    num yearsRetired = 0

    housekeeping()
    for y = 0 to yearsRemaining step 1
        if y <> 0 then
            savingBalance = savingBalance * INTEREST + annualSavings
        else
            savingBalance = annualSavings
        endif
    endfor
    endofjob()
END

housekeeping()
    output “Enter your remaining working years: “
    input yearsRemaining
    output “Enter the annual amount of money you can save: “
    input annualSavings
return

endofjob()
    while savingBalance > 0 AND yearsRetired <= MAX_RETIRE
        savingBalance = savingBalance - EXPENSES
        yearsRetired = yearsRetired + 1
        output “After year “ + yearsRetired + “you will have $“ + savingBalance + “ remaining in savings.” 
    endwhile
return
