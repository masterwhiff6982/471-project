import stripe

@app.post("/create-payment")
def handle_payment():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'bdt',
                'product_data': {'name': 'Daycare rent'},
                'unit_amount': 100000
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='',
    )
    return {"url": session.url}