START
    # DECLARATIONS
    num NUM_PRODUCTS = 5
    string PRODUCTS[NUM_PRODUCTS] = “Whipped Cream”, “Cinnamon”, “Chocolate Sauce”, “Amaretto”, “Irish Whiskey”
    num PRODUCTS_PRICES[NUM_PRODUCTS] = 0.89, 0.25, 0.59, 1.50, 1.75
    num BASIC_PRICE = 2.00
    string END_PROGRAM = “DONE”
    string INVALID_MSG = “Sorry, we do not carry that.”
    string PROMPT = “Please enter a add-in or DONE if your order is complete: “
    string userSelect = END_PROGRAM
    boolean validSelect = false
    num currentPrice

    housekeeping()
    do while userSelect <> END_PROGRAM
            updatePrice()
    endwhile
    endofjob()

END

housekeeping()
    currentPrice = BASIC_PRICE
    output PROMPT
    input = userSelect
return

updatePrice()
    validSelect = false
    for x = 0 to NUM_PRODUCTS -1 step 1
        if userSelect = PRODUCTS[x]
            validSelect = true
            currentPrice = currentPrice + PRODUCT_PRICES[x]
        endif
    endfor
    if validSelect = false then
        output INVALID_MSG
    endif
    output PROMPT
    input = userSelect 
return

endofjob()
    output “Your total price is $” + currentPrice
return
