<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Takım & Ürün Sayfası</title>
  <style>
    /* Reset & temel stiller */
    * {
      box-sizing: border-box;
      margin: 0; padding: 0;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    body {
      background: #f9fafb;
      color: #222;
      padding: 20px;
    }
    .container {
      max-width: 1100px;
      margin: auto;
    }

    /* Başlıklar */
    header {
      text-align: center;
      margin-bottom: 40px;
    }
    header h1 {
      font-size: 2.5rem;
      color: #004085;
      letter-spacing: 2px;
    }
    header p {
      font-size: 1.1rem;
      color: #555;
      margin-top: 10px;
    }

    /* Ürün bölümü */
    .product-section {
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
      margin-bottom: 60px;
    }
    .product-section h2 {
      margin-bottom: 20px;
      color: #004085;
    }
    .product-section p {
      font-size: 1rem;
      line-height: 1.6;
      color: #333;
    }

    /* Takım bölümü */
    .team-section {
      margin-bottom: 60px;
    }
    .team-section h2 {
      text-align: center;
      margin-bottom: 40px;
      color: #004085;
    }
    .team-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit,minmax(250px,1fr));
      gap: 25px;
    }
    .team-member {
      background: #fff;
      border-radius: 15px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      padding: 20px;
      text-align: center;
      transition: transform 0.3s ease;
      cursor: default;
    }
    .team-member:hover {
      transform: translateY(-8px);
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }
    .member-photo {
      width: 110px;
      height: 110px;
      border-radius: 50%;
      object-fit: cover;
      border: 3px solid #004085;
      margin-bottom: 15px;
      box-shadow: 0 3px 10px rgba(0,64,133,0.4);
    }
    .member-name {
      font-weight: 700;
      font-size: 1.3rem;
      color: #003366;
      margin-bottom: 6px;
    }
    .member-role {
      font-style: italic;
      font-size: 1rem;
      color: #555;
      margin-bottom: 12px;
    }
    .social-links {
      display: flex;
      justify-content: center;
      gap: 15px;
    }
    .social-links a {
      color: #555;
      font-size: 1.3rem;
      transition: color 0.3s ease;
    }
    .social-links a:hover {
      color: #004085;
    }

    /* Ürün özellikleri bölümü */
    .features-section {
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    .features-section h2 {
      text-align: center;
      margin-bottom: 30px;
      color: #004085;
    }
    .features-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit,minmax(280px,1fr));
      gap: 25px;
    }
    .feature-item {
      background: #e6f0ff;
      border-radius: 12px;
      padding: 20px;
      box-shadow: inset 0 0 8px rgba(0,64,133,0.15);
      transition: background 0.3s ease;
      display: flex;
      align-items: flex-start;
      gap: 15px;
    }
    .feature-item:hover {
      background: #cce0ff;
    }
    .feature-icon {
      flex-shrink: 0;
      width: 36px;
      height: 36px;
      fill: #004085;
      margin-top: 4px;
    }
    .feature-text h3 {
      margin-bottom: 8px;
      color: #003366;
      font-size: 1.15rem;
    }
    .feature-text p {
      font-size: 1rem;
      line-height: 1.5;
      color: #333;
    }

    /* Accordion bölümü */
    details {
      background: #fff;
      border-radius: 12px;
      padding: 18px 25px;
      margin-top: 25px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.08);
      cursor: pointer;
      transition: box-shadow 0.3s ease;
    }
    details[open] {
      box-shadow: 0 12px 30px rgba(0,0,0,0.15);
    }
    summary {
      font-weight: 700;
      font-size: 1.15rem;
      color: #004085;
      list-style: none;
      outline: none;
      user-select: none;
    }
    summary::-webkit-details-marker {
      display: none;
    }
    details[open] summary::after {
      content: "▲";
      float: right;
      font-size: 1rem;
      color: #004085;
    }
    summary::after {
      content: "▼";
      float: right;
      font-size: 1rem;
      color: #004085;
    }
    details p {
      margin-top: 15px;
      color: #333;
      line-height: 1.5;
      font-size: 1rem;
    }

    /* Responsive */
    @media (max-width: 600px) {
      .features-grid, .team-grid {
        grid-template-columns: 1fr;
      }
    }
  </style>
</head>
<body>
  <div class="container">

    <!-- Başlık -->
    <header>
      <h1>PROJE ADI</h1>
      <p>Kısa açıklama / slogan</p>
    </header>

    <!-- Ürün Tanımı -->
    <section class="product-section">
      <h2>Ürün Hakkında</h2>
      <p>Ürünün genel tanımı buraya gelecek.</p>
    </section>

    <!-- Takım Bölümü -->
    <section class="team-section">
      <h2>Takımımız</h2>
      <div class="team-grid">
        <article class="team-member">
          <img src="foto-url" alt="Üye İsmi" class="member-photo" />
          <h3 class="member-name">İsim Soyisim</h3>
          <p class="member-role">Görev / Rol</p>
          <div class="social-links">
            <a href="#" title="GitHub" aria-label="GitHub Link">🐙</a>
            <a href="#" title="LinkedIn" aria-label="LinkedIn Link">🔗</a>
          </div>
        </article>
        <!-- Buraya diğer takım üyeleri eklenir -->
      </div>
    </section>

    <!-- Ürün Özellikleri -->
    <section class="features-section">
      <h2>Özellikler</h2>
      <div class="features-grid">
        <div class="feature-item">
          <svg class="feature-icon" viewBox="0 0 24 24"><!-- ikon SVG --></svg>
          <div class="feature-text">
            <h3>Özellik Başlığı</h3>
            <p>Açıklama buraya gelecek.</p>
          </div>
        </div>
        <!-- Diğer özellikler -->
      </div>

      <!-- Accordion örnek -->
      <details>
        <summary>Detaylı Bilgi Başlığı</summary>
        <p>Bu kısımda detaylı açıklamalar olabilir.</p>
      </details>
      <details>
        <summary>Başka Bir Soru / Detay</summary>
        <p>İkinci detay açıklaması.</p>
      </details>
    </section>

  </div>
</body>
</html>
