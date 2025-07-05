<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Scrum Sprint Planı - README Güncelleme</title>
  <style>
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: #f9faff;
      color: #2c3e50;
      margin: 20px;
      line-height: 1.6;
    }
    header {
      text-align: center;
      margin-bottom: 30px;
      color: #34495e;
    }
    header h1 {
      font-size: 2.8rem;
      margin-bottom: 5px;
    }
    header p {
      font-size: 1.2rem;
      color: #7f8c8d;
    }
    section {
      background: white;
      border-radius: 10px;
      box-shadow: 0 6px 15px rgba(0,0,0,0.1);
      padding: 25px 30px;
      margin-bottom: 25px;
    }
    h2 {
      color: #2980b9;
      border-left: 6px solid #2980b9;
      padding-left: 10px;
      margin-bottom: 15px;
      font-weight: 700;
    }
    ul {
      list-style: none;
      padding-left: 0;
    }
    ul li {
      padding: 8px 0;
      border-bottom: 1px solid #ecf0f1;
      font-size: 1.1rem;
    }
    ul li:last-child {
      border-bottom: none;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
    table, th, td {
      border: 1px solid #bdc3c7;
    }
    th, td {
      padding: 12px 15px;
      text-align: left;
    }
    th {
      background-color: #2980b9;
      color: white;
      font-weight: 600;
    }
    code {
      background: #ecf0f1;
      padding: 3px 6px;
      border-radius: 4px;
      font-family: Consolas, monospace;
      font-size: 0.95rem;
    }
    footer {
      text-align: center;
      margin-top: 40px;
      color: #7f8c8d;
      font-style: italic;
      font-size: 0.9rem;
    }
    /* Emoji style */
    .emoji {
      font-size: 1.3rem;
      margin-right: 8px;
      vertical-align: middle;
    }
  </style>
</head>
<body>

  <header>
    <h1>🏁 Scrum Sprint Planı</h1>
    <p>README Güncelleme Projesi</p>
  </header>

  <section>
    <h2><span class="emoji">🎯</span> 1. Sprint Hedefi</h2>
    <p><strong>README dosyasını güncel ve anlaşılır hale getirmek.</strong> Projeye yeni katılan biri için rehber, kullanım kılavuzu ve proje bilgilerini netleştirmek.</p>
  </section>

  <section>
    <h2><span class="emoji">⏳</span> 2. Sprint Süresi</h2>
    <p><strong>1 Hafta (7 gün)</strong> — Kısa ve verimli tutarak gereksiz uzatmalardan kaçınmak.</p>
  </section>

  <section>
    <h2><span class="emoji">🗂️</span> 3. Sprint Backlog (Yapılacak İşler)</h2>
    <ul>
      <li><span class="emoji">📚</span> <strong>README Temel Yapısı Oluşturma</strong>: Proje tanıtımı, gereksinimler, kurulum adımları</li>
      <li><span class="emoji">⚙️</span> <strong>Fonksiyonel Kısımlar</strong>: Nasıl çalışır?, komut satırı örnekleri, branch stratejisi</li>
      <li><span class="emoji">📝</span> <strong>Dokümantasyon İyileştirme</strong>: Stil düzenlemesi, emoji & ikon ekleme, bağlantı güncelleme</li>
      <li><span class="emoji">🔍</span> <strong>Gözden Geçirme ve Onay</strong>: Takım review, son düzenlemeler, push</li>
    </ul>
  </section>

  <section>
    <h2><span class="emoji">📅</span> 4. Günlük Scrum (Daily Standup)</h2>
    <ul>
      <li>🕒 15 dakika hızlı toplantılar (her gün aynı saatte)</li>
      <li>Dün ne yaptım?</li>
      <li>Bugün ne yapacağım?</li>
      <li>Engelim var mı?</li>
    </ul>
  </section>

  <section>
    <h2><span class="emoji">🔄</span> 5. Sprint Review & Retrospective</h2>
    <ul>
      <li>Yapılan işleri göster (README güncellemeleri)</li>
      <li>Geri bildirim al</li>
      <li>Neler iyi gitti, neler geliştirilebilir?</li>
    </ul>
  </section>

  <section>
    <h2><span class="emoji">🚀</span> 6. Sprint Sonunda README Pushlama</h2>
    <p><code>git checkout main<br>
    git add README.md<br>
    git commit -m "README dosyası sprint #1 güncellemesi"<br>
    git push origin main</code></p>
  </section>

  <section>
    <h2><span class="emoji">🔥</span> Scrum Master için Öneriler</h2>
    <ul>
      <li>Sprint hedefini net tut</li>
      <li>Engelleri hemen tespit edip çözüm bul</li>
      <li>Takım iletişimini canlı tut, standupları aksatma</li>
      <li>Scope'u gerektiğinde küçültüp odaklanmayı sağla</li>
    </ul>
  </section>

  <section>
    <h2><span class="emoji">📊</span> Özet Tablo</h2>
    <table>
      <thead>
        <tr>
          <th>Aşama</th>
          <th>Sorumlu</th>
          <th>Süre</th>
          <th>Notlar</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Sprint Planlama</td>
          <td>Scrum Master</td>
          <td>1 saat</td>
          <td>Hedefleri belirle</td>
        </tr>
        <tr>
          <td>README Yazım</td>
          <td>Dev Team</td>
          <td>4 gün</td>
          <td>Parçaları böl ve bitir</td>
        </tr>
        <tr>
          <td>Daily Standup</td>
          <td>Tüm Takım</td>
          <td>Günlük 15 dk</td>
          <td>Takip ve destek</td>
        </tr>
        <tr>
          <td>Review & Retrospective</td>
          <td>Tüm Takım</td>
          <td>1 saat</td>
          <td>Geri bildirim & iyileştirme</td>
        </tr>
        <tr>
          <td>README Push</td>
          <td>Dev Team</td>
          <td>Sprint Sonu</td>
          <td>GitHub’a güncel hali yolla</td>
        </tr>
      </tbody>
    </table>
  </section>

  <footer>
    &copy; 2025 Scrum Master Plan • Hazırlayan: I0I
  </footer>

</body>
</html>
