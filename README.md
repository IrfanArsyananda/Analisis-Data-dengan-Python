# Dicoding - Belajar Analisis Data dengan Python

Link : https://www.dicoding.com/academies/555

# Preparing
<div class="mb-5 fr-view academy-tutorial-content content--prettify-light js-content-prettify">
    <ol>
        <li>Pertama, siapkan <em>environment&nbsp;</em>untuk menjalankan proyek ini. Pada proyek latihan ini, Anda dapat
            menggunakan berbagai IDE seperti Jupyter Notebook atau Google Colaboratory (Google Colab). Jika menjalankan
            latihan ini melalui Jupyter Notebook, pastikan Anda telah menginstal seluruh library yang dibutuhkan,
            seperti numpy, pandas, scipy, matplotlib, dan seaborn.<div class="table-responsive">
                <table class="table table-responsive" style="width:100%;">
                    <tbody>
                        <tr>
                            <td style="width:100%;">
                                <p dir="ltr"><strong>Saran</strong><br>Kami sangat menyarankan Anda untuk selalu membuat
                                    virtualenv baru pada setiap proyek. Hal ini untuk meminimalisasi masalah yang
                                    berhubungan dengan dependency pada library yang akan digunakan.</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <ol style="list-style-type:lower-alpha;">
                <li><strong>Membuat virtual environment menggunakan conda</strong><br>Apabila menginstal Python melalui
                    <a href="https://www.anaconda.com/products/distribution#Downloads" target="_blank"
                        rel="noreferrer noopener"><u>Anaconda</u></a> ataupun <a
                        href="https://docs.conda.io/en/latest/miniconda.html" target="_blank"
                        rel="noreferrer noopener"><u>miniconda</u></a>, Anda dapat menggunakan conda sebagai <em>package
                        manager</em> dan <em>environment management system</em>. Berikut merupakan tahapan dalam membuat
                    virtual environment menggunakan conda.<div class="table-responsive">
                        <table class="table table-responsive">
                            <tbody>
                                <tr>
                                    <td>
                                        <p dir="ltr">1.&nbsp;</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buka terminal atau PowerShell.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">2.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Jalankan perintah berikut.</p>
                                        <p dir="ltr"><strong>conda create --name main-ds python=3.9</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">3.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Aktifkan virtual environment dengan menjalankan perintah berikut.
                                        </p>
                                        <p dir="ltr"><strong>conda activate main-ds</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">4.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Instal semua library yang dibutuhkan menggunakan perintah berikut.
                                        </p>
                                        <p dir="ltr"><strong>p</strong><strong>ip install numpy pandas scipy matplotlib
                                                seaborn jupyter</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">5.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buka jupyter-notebook dengan menjalankan perintah berikut.</p>
                                        <p dir="ltr"><strong>jupyter-notebook .</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">6.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buat sebuah folder baru bernama
                                            <strong>proyek_analisis_data</strong>. Folder tersebut akan menjadi
                                            directory utama dalam proyek ini.&nbsp;
                                        </p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </li>
                <li><strong>Membuat virtual environment menggunakan pipenv</strong><br>Jika menginstal python melalui <a
                        href="https://www.python.org/" target="_blank" rel="noreferrer noopener"><u>official
                            home</u></a>, Anda dapat menggunakan pip sebagai package manager dan pipenv sebagai
                    environment management. Berikut merupakan tahapan dalam membuat virtual environment menggunakan
                    pipenv.<div class="table-responsive">
                        <table class="table table-responsive">
                            <tbody>
                                <tr>
                                    <td>
                                        <p dir="ltr">1.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buka terminal atau PowerShell.</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">2.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buat sebuah folder baru bernama
                                            <strong>proyek_analisis_data</strong> dengan menjalankan perintah berikut.
                                        </p>
                                        <p dir="ltr"><strong>mkdir proyek_analisis_data</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">3.&nbsp;</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Pindah ke folder terbaru tersebut menggunakan perintah berikut.</p>
                                        <p dir="ltr"><strong>cd proyek_analisis_data</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">4.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buat sebuah virtual environment dengan menjalankan perintah
                                            berikut.</p>
                                        <p dir="ltr"><strong>pipenv install</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">5.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Aktifkan virtual environment dengan menjalankan perintah berikut.
                                        </p>
                                        <p dir="ltr"><strong>pipenv shell</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">6.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Instal semua library yang dibutuhkan menggunakan perintah berikut.
                                        </p>
                                        <p dir="ltr"><strong>pip install numpy pandas scipy matplotlib seaborn
                                                jupyter</strong></p>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <p dir="ltr">7.</p>
                                    </td>
                                    <td>
                                        <p dir="ltr">Buka jupyter-notebook dengan menjalankan perintah berikut.</p>
                                        <p dir="ltr"><strong>jupyter-notebook .</strong></p>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </li>
            </ol>
        </li>
    </ol>
    <ol start="2">
        <li>Buat sebuah berkas baru bernama <strong>notebook.ipynb</strong>. Pada berkas inilah, seluruh proses analisis
            data akan dikerjakan.</li>
        <li>Buka berkas <strong>notebook.ipynb</strong>.</li>
        <li>Untuk memulai pengerjaan proyek ini, kita perlu memanggil semua library yang dibutuhkan. Berikut merupakan
            kode untuk melakukannya.
            <div class="prettyprint-wrapper">
                <button type="button" class="btn btn-secondary btn-sm btn-switch-prettyprint-theme">
                    <i class="icon fas fa-fw fa-moon"></i>
                </button>
                <pre class="prettyprint linenums prettyprinted"
                    style=""><ol class="linenums"><li class="L0"><span class="kwd">import</span><span class="pln"> numpy </span><span class="kwd">as</span><span class="pln"> np</span></li><li class="L1"><span class="kwd">import</span><span class="pln">&nbsp;pandas&nbsp;</span><span class="kwd">as</span><span class="pln">&nbsp;pd</span></li><li class="L2"><span class="kwd">import</span><span class="pln">&nbsp;matplotlib</span><span class="pun">.</span><span class="pln">pyplot&nbsp;</span><span class="kwd">as</span><span class="pln">&nbsp;plt</span></li><li class="L3"><span class="kwd">import</span><span class="pln"> seaborn </span><span class="kwd">as</span><span class="pln"> sns</span></li></ol></pre>
            </div>
        </li>
    </ol>
    <ol start="5">
        <li><em>Last but not least</em>, siapkan sebuah camilan sebagai suplai energi selama mengikuti latihan ini.</li>
    </ol>
    <p><br></p>
