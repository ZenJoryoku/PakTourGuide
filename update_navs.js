const fs = require('fs');
const path = require('path');

function updateFile(filename) {
    const filePath = path.join(__dirname, filename);
    const content = fs.readFileSync(filePath, 'utf8');

    // Regex to match the nav auth block up to </nav>
    const pattern = /<div class="flex items-center gap-3">\s*(?:<button|<div class="w-10)[\s\S]*?<\/div>\s*<\/div>\s*<\/nav>/g;

    const replacement = `<div class="flex items-center gap-3 nav-auth-container">
                        <div class="nav-loading w-10 h-10 flex items-center justify-center">
                            <div class="w-5 h-5 border-2 border-primary-500 border-t-transparent rounded-full animate-spin"></div>
                        </div>
                        <div class="nav-guest hidden flex items-center gap-3">
                            <button class="btn-outline !py-2 !px-6 !text-sm" onclick="openLoginModal()">Log In</button>
                            <button class="btn-primary !py-2 !px-6 !text-sm" onclick="navigateTo('signup')">Get Started</button>
                        </div>
                        <div class="nav-auth hidden flex items-center gap-3">
                            <div class="w-10 h-10 rounded-full bg-gradient-to-br from-primary-200 to-primary-400 overflow-hidden cursor-pointer shadow-lg hover:shadow-xl transition-all" onclick="navigateTo('account')">
                                <img src="https://images.unsplash.com/photo-1740252117013-4fb21771e7ca?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Nnx8cHJvZmlsZSUyMHBpYyUyMGVtcHR5fGVufDB8fDB8fHww" class="w-full h-full object-cover nav-profile-img rounded-full">
                            </div>
                        </div>
                    </div>
                </div>
            </nav>`;

    let matchCount = (content.match(pattern) || []).length;
    console.log(`Found ${matchCount} matches to replace in ${filename}`);

    if (matchCount > 0) {
        const newContent = content.replace(pattern, replacement);
        fs.writeFileSync(filePath, newContent, 'utf8');
        console.log(`Updated ${filename}`);
    }
}

updateFile('index.html');
updateFile('index2 (1).html');
