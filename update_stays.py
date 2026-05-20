import os

def update_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Navigation Links
    guides_link = """<a class="nav-link" href="#" onclick="navigateTo('guides');return false;">Guides</a>"""
    stays_link = """<a class="nav-link" href="#" onclick="navigateTo('stays');return false;">Stays</a>"""
    guides_link_active = """<a class="nav-link active" href="#" onclick="navigateTo('guides');return false;">Guides</a>"""
    
    content = content.replace(guides_link, guides_link + "\n                        " + stays_link)
    content = content.replace(guides_link_active, guides_link_active + "\n                        " + stays_link)

    # 2. Insert Stays Section before contact section
    contact_section_start = """    <section id="contact" class="page">"""
    
    stays_section = """
    <!-- STAYS PAGE -->
    <section id="stays" class="page">
        <div class="pt-28 pb-20 hero-gradient relative overflow-hidden">
            <div class="absolute inset-0 bg-[url('https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80')] bg-cover bg-center opacity-20"></div>
            <div class="absolute inset-0 bg-gradient-to-b from-transparent to-[#1a0533]/90"></div>
            <div class="container mx-auto px-6 relative z-10">
                <div class="max-w-3xl">
                    <h1 class="text-4xl md:text-6xl font-black text-white mb-6 leading-tight animate-slide-up">
                        Find the Perfect <span class="text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-pink-500">Stay</span>
                    </h1>
                    <p class="text-xl text-gray-300 mb-10 font-medium animate-slide-up" style="animation-delay: 0.1s;">
                        Comfortable rooms, gorgeous guesthouses, and unforgettable accommodations.
                    </p>
                    
                    <!-- Host Only Button -->
                    <div id="host-stays-controls" class="hidden animate-slide-up" style="animation-delay: 0.2s;">
                        <button class="btn-primary !px-8 !py-4" onclick="document.getElementById('stay-registration-modal').classList.add('active')">
                            + Add More Cards / Register Stays
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div class="container mx-auto px-6 py-20">
            <div class="flex justify-between items-end mb-12">
                <div>
                    <h2 class="text-3xl font-black text-gray-900 mb-2">Available Rooms</h2>
                    <p class="text-gray-500">Book your next comfortable stay</p>
                </div>
            </div>

            <div id="stays-grid" class="grid md:grid-cols-3 gap-8">
                <!-- Stays Cards will be injected here -->
            </div>
        </div>
    </section>
"""
    if 'id="stays"' not in content:
        content = content.replace(contact_section_start, stays_section + "\n" + contact_section_start)

    # 3. Add Modals near the end of body
    modals = """
    <!-- STAY REGISTRATION MODAL (HOSTS) -->
    <div id="stay-registration-modal" class="modal-overlay">
        <div class="modal-content relative overflow-hidden">
            <div class="p-8">
                <button class="absolute top-6 right-6 text-gray-400 hover:text-gray-600 transition-colors"
                    onclick="document.getElementById('stay-registration-modal').classList.remove('active')">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <h2 class="text-3xl font-black text-gray-900 mb-2">Register a Stay</h2>
                <p class="text-gray-500 mb-8">List your room or guesthouse for travellers.</p>
                
                <form id="stay-registration-form" onsubmit="window.registerStay(event)" class="space-y-5">
                    <div>
                        <label class="block text-sm font-bold text-gray-700 mb-2">Hotel / Guesthouse Name</label>
                        <input type="text" id="stay-name" class="input-field" required placeholder="e.g. Serena Guest House">
                    </div>
                    <div>
                        <label class="block text-sm font-bold text-gray-700 mb-2">Room Picture URL</label>
                        <input type="url" id="stay-image" class="input-field" required placeholder="https://images.unsplash.com/...">
                    </div>
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-2">Number of Beds</label>
                            <input type="number" id="stay-beds" min="1" class="input-field" required placeholder="e.g. 2">
                        </div>
                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-2">Price per Night (PKR)</label>
                            <input type="number" id="stay-price" min="1" class="input-field" required placeholder="e.g. 4500">
                        </div>
                    </div>
                    <div>
                        <label class="block text-sm font-bold text-gray-700 mb-2">Location / City</label>
                        <select id="stay-city" class="input-field" required>
                            <option value="">Select City</option>
                            <option value="Karachi">Karachi</option>
                            <option value="Lahore">Lahore</option>
                            <option value="Islamabad">Islamabad</option>
                            <option value="Skardu">Skardu</option>
                            <option value="Hunza">Hunza</option>
                            <option value="Swat">Swat</option>
                            <option value="Fairy Meadows">Fairy Meadows</option>
                        </select>
                    </div>
                    
                    <button type="submit" class="btn-primary !w-full !py-4 mt-4" id="stay-register-btn">
                        Publish Stay
                    </button>
                </form>
            </div>
        </div>
    </div>

    <!-- STAY BOOKING MODAL (TRAVELLERS) -->
    <div id="stay-booking-modal" class="modal-overlay">
        <div class="modal-content relative overflow-hidden">
            <div class="p-8">
                <button class="absolute top-6 right-6 text-gray-400 hover:text-gray-600 transition-colors"
                    onclick="document.getElementById('stay-booking-modal').classList.remove('active')">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <h2 class="text-3xl font-black text-gray-900 mb-2">Book Room</h2>
                <p id="stay-booking-subtitle" class="text-gray-500 mb-8">Select dates to calculate total.</p>
                
                <form id="stay-booking-form" onsubmit="window.submitStayBooking(event)" class="space-y-5">
                    <input type="hidden" id="stay-booking-id">
                    <input type="hidden" id="stay-booking-price">
                    <div class="grid grid-cols-2 gap-4">
                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-2">Check-in</label>
                            <input type="date" id="stay-checkin" class="input-field" required onchange="window.calculateStayTotal()">
                        </div>
                        <div>
                            <label class="block text-sm font-bold text-gray-700 mb-2">Check-out</label>
                            <input type="date" id="stay-checkout" class="input-field" required onchange="window.calculateStayTotal()">
                        </div>
                    </div>
                    
                    <div class="mt-6 p-6 bg-gray-50 rounded-2xl border border-gray-100">
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-gray-600">Price per night</span>
                            <span id="stay-booking-ppn" class="font-bold">PKR 0</span>
                        </div>
                        <div class="flex justify-between items-center mb-2">
                            <span class="text-gray-600">Nights</span>
                            <span id="stay-booking-nights" class="font-bold">0</span>
                        </div>
                        <div class="h-px w-full bg-gray-200 my-4"></div>
                        <div class="flex justify-between items-center">
                            <span class="font-black text-lg text-gray-900">Total</span>
                            <span id="stay-booking-total" class="font-black text-2xl text-primary-600">PKR 0</span>
                        </div>
                    </div>
                    
                    <button type="submit" class="btn-primary !w-full !py-4 mt-4" id="stay-confirm-btn">
                        Confirm Booking
                    </button>
                </form>
            </div>
        </div>
    </div>
"""
    body_end = "</body>"
    if 'id="stay-registration-modal"' not in content:
        content = content.replace(body_end, modals + "\n" + body_end)


    # 4. JavaScript Logic Injection
    # We will insert it inside the `<script>` block that ends near the bottom.
    # Looking for a suitable insertion point. Let's insert before `</script>` which is right before `</body>`
    
    js_logic = """
        // --- STAYS FUNCTIONALITY ---
        let stays = [];

        // Load Stays from Firestore
        import { getFirestore, collection, addDoc, getDocs, onSnapshot, serverTimestamp } from "https://www.gstatic.com/firebasejs/12.12.1/firebase-firestore.js";
        const db = getFirestore();

        function loadStays() {
            const staysRef = collection(db, 'stays');
            onSnapshot(staysRef, (snapshot) => {
                stays = [];
                snapshot.forEach((doc) => {
                    stays.push({ id: doc.id, ...doc.data() });
                });
                if (window.currentPage === 'stays') {
                    window.renderStays();
                }
            }, (error) => {
                console.error("Error loading stays:", error);
            });
        }

        window.renderStays = () => {
            const grid = document.getElementById('stays-grid');
            if (!grid) return;
            
            if (stays.length === 0) {
                grid.innerHTML = '<div class="col-span-full text-center py-10 text-gray-500">No rooms registered yet.</div>';
                return;
            }

            grid.innerHTML = stays.map(s => {
                return `
                <div class="card overflow-hidden">
                    <div class="relative h-64 w-full bg-gray-200">
                        <img src="${s.image}" alt="${s.hotelName}" class="w-full h-full object-cover" style="object-position: center; width: 100%; height: 100%; object-fit: cover;">
                        <div class="absolute inset-0 bg-gradient-to-t from-black/70 to-transparent"></div>
                        <div class="absolute bottom-4 left-4 text-white">
                            <h3 class="text-xl font-bold">${s.hotelName}</h3>
                            <p class="text-sm badge bg-primary-500 text-white mt-1 border-none">${s.city.toUpperCase()}</p>
                        </div>
                    </div>
                    <div class="p-5">
                        <p class="text-gray-600 mb-4 font-medium">Guesthouse Room • ${s.beds} Beds</p>
                        <div class="flex justify-between items-center mb-4">
                            <span class="text-sm text-gray-500">Per night</span>
                            <span class="text-xl font-bold text-primary-600">PKR ${Number(s.pricePerNight).toLocaleString()}</span>
                        </div>
                        <div class="flex gap-3">
                            <button class="btn-primary !w-full !rounded-xl !py-3" onclick="window.openStayBookingModal('${s.id}')">
                                Book Room
                            </button>
                        </div>
                    </div>
                </div>`;
            }).join('');
        };

        window.registerStay = async (e) => {
            e.preventDefault();
            const btn = document.getElementById('stay-register-btn');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span class="animate-pulse">Publishing...</span>';
            btn.disabled = true;

            try {
                if (!window.currentUser || window.currentUser.role !== 'guide') {
                    throw new Error("Only guides/hosts can register stays.");
                }

                const stayData = {
                    hotelName: document.getElementById('stay-name').value,
                    image: document.getElementById('stay-image').value,
                    beds: parseInt(document.getElementById('stay-beds').value),
                    pricePerNight: parseFloat(document.getElementById('stay-price').value),
                    city: document.getElementById('stay-city').value,
                    hostId: window.currentUser.uid,
                    createdAt: serverTimestamp()
                };

                await addDoc(collection(db, 'stays'), stayData);
                
                showToast('Stay published successfully!', 'success');
                document.getElementById('stay-registration-modal').classList.remove('active');
                document.getElementById('stay-registration-form').reset();
            } catch (error) {
                console.error("Error adding stay:", error);
                showToast('Failed to publish stay: ' + error.message, 'error');
            } finally {
                btn.innerHTML = originalText;
                btn.disabled = false;
            }
        };

        window.openStayBookingModal = (stayId) => {
            if (!window.currentUser) {
                showToast('Please login to book a room.', 'warning');
                navigateTo('signup');
                return;
            }

            const stay = stays.find(s => s.id === stayId);
            if (!stay) return;

            document.getElementById('stay-booking-id').value = stay.id;
            document.getElementById('stay-booking-price').value = stay.pricePerNight;
            document.getElementById('stay-booking-subtitle').textContent = `Booking ${stay.hotelName} in ${stay.city}`;
            document.getElementById('stay-booking-ppn').textContent = `PKR ${Number(stay.pricePerNight).toLocaleString()}`;
            
            // Reset fields
            document.getElementById('stay-checkin').value = '';
            document.getElementById('stay-checkout').value = '';
            document.getElementById('stay-booking-nights').textContent = '0';
            document.getElementById('stay-booking-total').textContent = 'PKR 0';

            document.getElementById('stay-booking-modal').classList.add('active');
        };

        window.calculateStayTotal = () => {
            const checkin = new Date(document.getElementById('stay-checkin').value);
            const checkout = new Date(document.getElementById('stay-checkout').value);
            const price = parseFloat(document.getElementById('stay-booking-price').value);

            if (checkin && checkout && checkout > checkin) {
                const diffTime = Math.abs(checkout - checkin);
                const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
                document.getElementById('stay-booking-nights').textContent = diffDays;
                document.getElementById('stay-booking-total').textContent = `PKR ${(diffDays * price).toLocaleString()}`;
            } else {
                document.getElementById('stay-booking-nights').textContent = '0';
                document.getElementById('stay-booking-total').textContent = 'PKR 0';
            }
        };

        window.submitStayBooking = async (e) => {
            e.preventDefault();
            const btn = document.getElementById('stay-confirm-btn');
            const originalText = btn.innerHTML;
            btn.innerHTML = '<span class="animate-pulse">Confirming...</span>';
            btn.disabled = true;

            try {
                const checkin = new Date(document.getElementById('stay-checkin').value);
                const checkout = new Date(document.getElementById('stay-checkout').value);
                if (!checkin || !checkout || checkout <= checkin) {
                    throw new Error("Invalid dates selected.");
                }

                const price = parseFloat(document.getElementById('stay-booking-price').value);
                const diffTime = Math.abs(checkout - checkin);
                const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 
                const total = diffDays * price;
                const stayId = document.getElementById('stay-booking-id').value;
                const stay = stays.find(s => s.id === stayId);

                const bookingData = {
                    userId: window.currentUser.uid,
                    stayId: stayId,
                    hotelName: stay.hotelName,
                    city: stay.city,
                    checkin: document.getElementById('stay-checkin').value,
                    checkout: document.getElementById('stay-checkout').value,
                    nights: diffDays,
                    total: total,
                    type: 'stay',
                    createdAt: serverTimestamp()
                };

                await addDoc(collection(db, 'bookings'), bookingData);
                
                showToast('Room booked successfully!', 'success');
                document.getElementById('stay-booking-modal').classList.remove('active');
                
                // Add booking visually if possible or just navigate
                navigateTo('my-bookings');
            } catch (error) {
                console.error("Error booking room:", error);
                showToast(error.message || 'Failed to book room', 'error');
            } finally {
                btn.innerHTML = originalText;
                btn.disabled = false;
            }
        };

        // Initialize stays listener
        setTimeout(loadStays, 2000);
"""

    if 'window.renderStays =' not in content:
        # Find the last </script> in the file
        last_script_tag = content.rfind("    </script>")
        if last_script_tag != -1:
            content = content[:last_script_tag] + js_logic + "\n" + content[last_script_tag:]

    # Update navigateTo function inside content to handle stays
    # We find: if (pageId === 'guides') renderGuides('all');
    navigate_guides_logic = "if (pageId === 'guides') renderGuides('all');"
    navigate_stays_logic = "if (pageId === 'stays') window.renderStays();"
    if navigate_stays_logic not in content:
        content = content.replace(navigate_guides_logic, navigate_guides_logic + "\n                " + navigate_stays_logic)
        
    # Find updateNavProfile or auth state change to toggle the register stays button
    # window.updateNavProfile = () => {
    auth_host_logic = """
            if (window.currentUser && window.currentUser.role === 'guide') {
                const hostControls = document.getElementById('host-stays-controls');
                if(hostControls) hostControls.classList.remove('hidden');
            } else {
                const hostControls = document.getElementById('host-stays-controls');
                if(hostControls) hostControls.classList.add('hidden');
            }
"""
    update_nav_profile_start = "window.updateNavProfile = () => {"
    if 'host-stays-controls' not in content.split(update_nav_profile_start)[-1][:500] and update_nav_profile_start in content:
        content = content.replace(update_nav_profile_start, update_nav_profile_start + "\n" + auth_host_logic)


    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Successfully updated {filepath}")

update_file(r"c:\Users\DELL\OneDrive\Desktop\PTG Final\index.html")
update_file(r"c:\Users\DELL\OneDrive\Desktop\PTG Final\index2 (1).html")
