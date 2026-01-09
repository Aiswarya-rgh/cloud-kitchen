// ===========================================
// FRONTEND LOGIC (The Brains)
// ===========================================

const API_URL = "http://127.0.0.1:8000";

// 1. Fetch Kitchens when page loads
document.addEventListener('DOMContentLoaded', async () => {
    const kitchenList = document.getElementById('kitchen-list');

    try {
        // A. Call the Server
        const response = await fetch(`${API_URL}/kitchens`);

        if (!response.ok) {
            throw new Error("Server not responding");
        }

        const kitchens = await response.json();

        // B. Clear Loading Text
        kitchenList.innerHTML = '';

        // C. Loop through data and create HTML cards
        kitchens.forEach(kitchen => {
            const card = createKitchenCard(kitchen);
            kitchenList.appendChild(card);
        });

    } catch (error) {
        console.error("Error:", error);
        kitchenList.innerHTML = `<p style="color: red; text-align: center;">❌ Failed to load kitchens. Is the backend running?</p>`;
    }
});

// 2. Helper function to create HTML for one kitchen
function createKitchenCard(kitchen) {
    const div = document.createElement('div');
    div.className = 'kitchen-card';

    // Random placeholder image for now
    const randomImage = `https://source.unsplash.com/400x300/?food,cooking,${kitchen.cuisine_type}`;

    div.innerHTML = `
        <div class="card-image" style="background-image: url('https://images.unsplash.com/photo-1556910103-1c02745a30bf')"></div>
        <div class="card-content">
            <span class="card-badge">${kitchen.cuisine_type || 'General'}</span>
            <h3 class="card-title">${kitchen.name}</h3>
            <p class="card-info">By ${kitchen.owner_name}</p>
            <p class="card-description" style="color: #888; font-size: 0.9em; margin-bottom: 15px;">
                ${kitchen.description || "No description available."}
            </p>
            <a href="#" class="btn-primary" onclick="alert('Menu page coming in Step 8! ID: ${kitchen._id}')">View Menu</a>
        </div>
    `;
    return div;
}
