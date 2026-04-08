# SDSWEAR.ID - Website Profile Flask

Website profile modern dan profesional untuk SDSWEAR.ID yang dibangun dengan Flask, Jinja2, HTML, CSS, dan JavaScript vanilla.

## Fitur

- **Modern Design**: Tampilan profesional dengan color palette navy dan orange
- **Responsive**: Sempurna di semua ukuran layar (mobile, tablet, desktop)
- **Interactive Elements**: Animasi halus, hover effects, dan smooth transitions
- **SEO Friendly**: Meta tags yang optimal untuk search engines
- **Contact Form**: Form kontak yang fungsional dengan validasi
- **Fast Loading**: CSS dan JS yang minimal dan optimal
- **Mobile Navigation**: Navigation menu yang responsif dengan hamburger menu

## Struktur Project

```
sdswear-id/
├── app.py                  # Flask main application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── templates/             # Jinja2 templates
│   ├── base.html          # Base template (header, footer, navigation)
│   ├── index.html         # Home page
│   ├── 404.html           # 404 error page
│   └── 500.html           # 500 error page
└── static/                # Static files
    ├── css/
    │   └── style.css      # Main stylesheet
    └── js/
        └── main.js        # Main JavaScript
```

## Instalasi

### Persyaratan
- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone repository atau download project**
```bash
cd sdswear-id
```

2. **Buat virtual environment**
```bash
python -m venv venv
```

3. **Aktifkan virtual environment**

Untuk Windows:
```bash
venv\Scripts\activate
```

Untuk macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Run Flask application**
```bash
python app.py
```

6. **Buka browser** dan kunjungi `http://localhost:5000`

## Penggunaan

### Menjalankan di Development Mode
```bash
python app.py
```

Aplikasi akan berjalan di `http://localhost:5000` dengan debug mode aktif.

### Deployment

Untuk deploy ke production, Anda bisa menggunakan:
- **Heroku**: Gratis atau berbayar
- **PythonAnywhere**: Hosting Python khusus
- **Vercel**: Serverless platform
- **AWS**: Amazon Web Services
- **DigitalOcean**: VPS affordable
- **Railway**: Modern PaaS platform

## Customization

### Mengubah Warna

Edit file `static/css/style.css` dan ubah root variables:

```css
:root {
    --primary-color: #1e3a5f;      /* Warna biru navy */
    --accent-color: #d97706;       /* Warna orange */
    /* ... warna lainnya ... */
}
```

### Mengubah Content

Edit file `templates/index.html` untuk:
- Mengubah teks dan heading
- Menambah/mengurangi sections
- Update portfolio items
- Customize testimonials

### Mengubah Contact Form

Edit `app.py` di function `handle_contact()` untuk:
- Menambah validasi lebih ketat
- Mengintegrasikan dengan email service
- Menyimpan data ke database

## Fitur-Fitur

### 1. Hero Section
- Headline yang menarik
- Call-to-action buttons
- Feature cards highlight

### 2. Services Section
- 6 layanan dengan icon dan deskripsi
- Grid layout responsif
- Hover effects interaktif

### 3. Portfolio Section
- Showcase 6 project terbaik
- Gradient backgrounds yang unik
- Tag kategori untuk setiap project

### 4. Why Us Section
- 6 alasan memilih SDSWEAR.ID
- Check mark icon styling
- Hover animation effects

### 5. Testimonials
- 3 testimonial dari clients
- Star rating display
- Professional layout

### 6. Contact Section
- Form input validation
- Success/error messaging
- Contact information
- Business hours

### 7. Responsive Navigation
- Fixed header dengan blur effect
- Mobile hamburger menu
- Smooth scroll anchor links
- Active link indicators

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Android)

## Performance

- Optimized CSS (772 lines)
- Minimal JavaScript (158 lines)
- No external dependencies (pure vanilla JS)
- Fast loading time
- Lighthouse optimized

## Security

- CSRF protection ready (dapat ditambahkan dengan Flask-WTF)
- Input validation pada contact form
- Sanitized output dengan Jinja2

## Future Enhancements

Fitur yang dapat ditambahkan:
- [ ] Database integration (SQLAlchemy, SQLite, PostgreSQL)
- [ ] Email notifications (Flask-Mail)
- [ ] Admin panel (Flask-Admin)
- [ ] Blog/News section
- [ ] Multi-language support (i18n)
- [ ] Analytics integration (Google Analytics)
- [ ] Customer reviews management
- [ ] Product catalog dengan detail
- [ ] Shopping cart functionality
- [ ] Payment integration (Stripe, Midtrans)

## Troubleshooting

### Port 5000 already in use
```bash
python app.py --port 8000
```

### ModuleNotFoundError
Pastikan Anda sudah mengaktifkan virtual environment dan install requirements:
```bash
pip install -r requirements.txt
```

### Template not found error
Pastikan struktur folder `templates/` benar dan file `.html` ada di folder tersebut.

## License

MIT License - Feel free to use this project for personal and commercial use.

## Contact

- Email: info@sdswear.id
- Phone: +62 812-3456-7890
- Location: Jakarta, Indonesia

## Author

Dibuat dengan ❤️ untuk SDSWEAR.ID menggunakan Flask dan modern web technologies.
