// src/frontend/src/components/Payments/Payment.js

import React from "react";
import axios from "axios";

const Payment = ({ amount, email }) => {
    const handlePayment = async () => {
        try {
            // Initialize payment
            const response = await axios.post("/payments/initialize/", { amount, email });
            const { authorization_url, reference } = response.data.data;

            // Open Paystack payment modal
            const handler = window.PaystackPop.setup({
                key: "your_paystack_public_key",
                email: email,
                amount: amount * 100,  // amount in kobo
                currency: "NGN",
                ref: reference,
                callback: function (response) {
                    verifyPayment(response.reference);
                },
                onClose: function () {
                    alert("Payment window closed.");
                },
            });
            handler.openIframe();
        } catch (error) {
            console.error("Payment initialization error:", error);
        }
    };

    const verifyPayment = async (reference) => {
        try {
            // Verify payment
            const response = await axios.get(`/payments/verify/${reference}/`);
            if (response.data.status === "success") {
                alert("Payment successful!");
            } else {
                alert("Payment verification failed.");
            }
        } catch (error) {
            console.error("Payment verification error:", error);
        }
    };

    return (
        <button onClick={handlePayment}>Pay Now</button>
    );
};

export default Payment;
