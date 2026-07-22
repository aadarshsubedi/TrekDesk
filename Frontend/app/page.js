"use client";

import { useState, useEffect } from "react";

const API_URL = "http://127.0.0.1:8000";

const emptyForm = {
  client_name: "",
  trek_route: "",
  start_date: "",
  no_of_people: "",
  deposit_paid: false,
};

export default function Home() {
  const [bookings, setBookings] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  const [formData, setFormData] = useState(emptyForm);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitError, setSubmitError] = useState(null);

  function fetchBookings() {
    setIsLoading(true);
    setError(null);
    fetch(`${API_URL}/bookings`)
      .then((res) => {
        if (!res.ok) {
          throw new Error("Server responded with an error");
        }
        return res.json();
      })
      .then((data) => {
        setBookings(data);
        setIsLoading(false);
      })
      .catch(() => {
        setError("Couldn't load bookings. Is the server running?");
        setIsLoading(false);
      });
  }

  useEffect(() => {
    fetchBookings();
  }, []);

  function handleChange(event) {
    const { name, value, type, checked } = event.target;
    setFormData((prev) => ({
      ...prev,
      [name]: type === "checkbox" ? checked : value,
    }));
  }

  function handleSubmit(event) {
    event.preventDefault();
    setIsSubmitting(true);
    setSubmitError(null);

    fetch(`${API_URL}/bookings`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        ...formData,
        no_of_people: Number(formData.no_of_people),
      }),
    })
      .then((res) => {
        if (!res.ok) {
          return res.json().then((data) => {
            throw new Error(JSON.stringify(data));
          });
        }
        return res.json();
      })
      .then(() => {
        setFormData(emptyForm);
        setIsSubmitting(false);
        fetchBookings();
      })
      .catch((err) => {
        console.error("Booking creation failed:", err.message);
        setSubmitError(
          "Couldn't create booking. Check the fields and try again."
        );
        setIsSubmitting(false);
      });
  }

  return (
    <main>
      <h1>TrekDesk</h1>

      <section>
        <h2>Add a booking</h2>
        <form onSubmit={handleSubmit}>
          <label>
            Client name
            <input
              type="text"
              name="client_name"
              value={formData.client_name}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Trek route
            <input
              type="text"
              name="trek_route"
              value={formData.trek_route}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            Start date
            <input
              type="date"
              name="start_date"
              value={formData.start_date}
              onChange={handleChange}
              required
            />
          </label>

          <label>
            No of people
            <input
              type="number"
              name="no_of_people"
              value={formData.no_of_people}
              onChange={handleChange}
              min="1"
              required
            />
          </label>

          <label>
            <input
              type="checkbox"
              name="deposit_paid"
              checked={formData.deposit_paid}
              onChange={handleChange}
            />
            Deposit paid
          </label>

          <button type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Adding..." : "Add booking"}
          </button>

          {submitError && <p className="error-text">{submitError}</p>}
        </form>
      </section>

      <section>
        <h2>Upcoming bookings</h2>

        {isLoading && <p className="status-text">Loading bookings...</p>}
        {error && <p className="error-text">{error}</p>}

        {!isLoading && !error && (
          <ul>
            {bookings.map((booking) => (
              <li key={booking.id}>
                <div className="booking-client">{booking.client_name}</div>
                <div className="booking-meta">
                  {booking.trek_route} · {booking.start_date}
                </div>
              </li>
            ))}
          </ul>
        )}
      </section>
    </main>
  );
}