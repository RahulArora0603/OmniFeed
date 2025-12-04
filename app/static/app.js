let current_topic = "artificial intelligence"

function loadContent(type, topic= current_topic) {

    const content = document.getElementById("content");

    content.innerHTML = `
    <div class="text-center my-4">
        <div class="spinner-border text-primary" role="status"></div>
    </div>    
    `;

    const query = encodeURIComponent(topic || "artificial intelligence");
    const url = `/${type}?query=${query}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            // const content = document.getElementById("content");
            // content.innerHTML = "";

            content.innerHTML = '<div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4"></div>';
            const row = content.querySelector('.row');
            
            //const placeholder = "/static/images/pngtree-science-and-technology-future-high-tech-light-background-sci-fi-picture-image_2247992.jpg";
            console.log("Fetched data:", data);

            data.forEach(item => {
                const col = document.createElement("div");
                col.classList.add("col");

                const card = document.createElement("div");
                card.classList.add("card","h-100","shadow","border-0","shadow-sm","custom-card");

                // Add subtle gradient background to the card
                card.style.background = "linear-gradient(145deg, #ffffff , #f9f9f9)";
                card.style.borderRadius = "16px";
                card.style.overflow = "hidden";
                card.style.transition = "transform 0.3s ease, box-shadow 0.3s ease";

                // hover animation
                card.addEventListener("mouseover", () => {
                    card.style.transform = "translateY(-6px)";
                    card.style.boxShadow = "0 10px 20px rgba(0,0,0, 0.15)";
                });
                card.addEventListener("mouseout", () => {
                    card.style.transform = "translateY(0)";
                    card.style.boxShadow = "0 4px 8px rgba(0,0,0,0.05)";
                });
                /*if (type === "reddit" || type === "news" || type === "papers") {
                    /*const imageUrl = item.image; /*? item.image : placeholder;
                    console.log(imageUrl)
                    let imageUrl = item.image;
                    if (!imageUrl || imageUrl === "null" || imageUrl === null) {
                        imageUrl = placeholder;
                    }

                    console.log("Image URL:", imageUrl);
                    div.innerHTML = `<img src="${imageUrl}" alt="News Image" class="card-img" style="width:100%; height:auto;"><h3>${item.title}</h3><h6>Abcd</h6><a href="${item.url}" target="_blank">Read more</a>`;
                }
                else if (type === "twitter") {
                    div.innerHTML = `<p>${item.text}</p>`;
                }
                content.appendChild(div);*/
                let placeholder;
                if (item.name==="Reddit"){
                    placeholder = "/static/images/Reddit-Logo.jpg"
                }
                else if (item.name==="NewsAPI"){
                    placeholder = "/static/images/pngtree-global-news-glyph-icon-news-network-logo-vector-png-image_41818854.jpg"
                }
                else if (item.name==="YouTube"){
                    placeholder = "/static/images/YouTube-Logo.png"
                }
                else if (item.name==="Research"){
                    placeholder = "/static/images/291-2918679_research-paper-logo-png-transparent-png.png"
                }
                else {
                    placeholder = "/static/images/Medium-Logo.jpg"
                }
                let imageUrl = item.image;
                // const placeholder = ""; // Update path if needed
                if (!imageUrl || imageUrl === "null" || imageUrl === null) {
                    imageUrl = placeholder;
                }
            
                const img = document.createElement("img");
                img.src = imageUrl;
                img.classList.add("card-img-top");
                img.alt = "Image";
                img.style.height = "200px";
                img.style.objectFit = "cover";
                img.style.transition = "transform 0.4s ease";
                img.addEventListener("mouseover", () => (img.style.transform = "scale(1.5)"));
                img.addEventListener("mouseout", () => (img.style.transform = "scale(1)"));            
                const cardBody = document.createElement("div");
                cardBody.classList.add("card-body", "d-flex", "flex-column", "justify-content-between");
            
                const title = document.createElement("h5");
                title.classList.add("card-title", "fw-semibold");
                title.textContent = item.title;
                title.style.color = "#212529";
            
                const link = document.createElement("a");
                link.href = item.url;
                link.target = "_blank";
                link.classList.add("btn", "btn-primary", "mt-2","w-100");
                link.textContent = "Read more";

                cardBody.appendChild(title);
                cardBody.appendChild(link);
                // cardBody.appendChild(saveBtn);

                card.appendChild(img);
                card.appendChild(cardBody);
                col.appendChild(card);
                row.appendChild(col);
            });
        });
}

function searchNews(){
    const input = document.getElementById("searchInput").value.trim();
    current_topic = input || "artificial intelligence";
    loadContent("news");
}
