# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    # =========================
    # Kameez
    # =========================
    lambai_kameez = fields.Char(string="لمبائی", tracking=True)
    shoulder_kameez = fields.Char(string="شولڈر / کندھا", tracking=True)
    bazu_kameez = fields.Char(string="بازو", tracking=True)
    galla_kameez = fields.Char(string="گلا", tracking=True)
    chaati_kameez = fields.Char(string="چھاتی", tracking=True)
    daaman_kameez = fields.Char(string="دامن", tracking=True)
    shalwar_lambai_kameez = fields.Char(string="شلوار لمبائی", tracking=True)
    shalwar_pancha_kameez = fields.Char(string="شلوار پنجہ", tracking=True)
    additional_notes_kameez = fields.Char(string="اضافی نوٹس", tracking=True)

    # =========================
    # Shirt
    # =========================
    lambai_shirt = fields.Char(string="لمبائی", tracking=True)
    shoulder_shirt = fields.Char(string="شولڈر / کندھا", tracking=True)
    bazu_shirt = fields.Char(string="بازو", tracking=True)
    galla_shirt = fields.Char(string="گلا", tracking=True)
    chaati_shirt = fields.Char(string="چھاتی", tracking=True)
    daaman_shirt = fields.Char(string="دامن", tracking=True)
    front_pocket_shirt = fields.Char(string="فرنٹ پاکٹ", tracking=True)
    double_cuff_shirt = fields.Char(string="ڈبل کف", tracking=True)
    double_pocket_shoulder_shirt = fields.Char(string="ڈبل پاکٹ شولڈر", tracking=True)
    additional_notes_shirt = fields.Char(string="اضافی نوٹس", tracking=True)

    # =========================
    # Pant
    # =========================
    lambai_pant = fields.Char(string="لمبائی", tracking=True)
    kamar_pant = fields.Char(string="کمر", tracking=True)
    hip_pant = fields.Char(string="ہِپ", tracking=True)
    gadri_pant = fields.Char(string="گدری", tracking=True)
    goda_pant = fields.Char(string="گھٹنا", tracking=True)
    mori_pant = fields.Char(string="موڑی", tracking=True)
    baghair_plait_pant = fields.Char(string="بغیر پلیٹ", tracking=True)
    double_plait_pant = fields.Char(string="ڈبل پلیٹ", tracking=True)
    gam_pati_pant = fields.Char(string="گم پٹی", tracking=True)
    additional_notes_pant = fields.Char(string="اضافی نوٹس", tracking=True)

    # =========================
    # Coat / Waist Coat
    # =========================
    lambai_coat = fields.Char(string="لمبائی", tracking=True)
    teera_coat = fields.Char(string="تیرا", tracking=True)
    chaati_coat = fields.Char(string="چھاتی", tracking=True)
    bazu_coat = fields.Char(string="بازو", tracking=True)
    kamar_coat = fields.Char(string="کمر", tracking=True)
    hip_coat = fields.Char(string="ہِپ", tracking=True)
    side_chaak_coat = fields.Char(string="سائیڈ چاک", tracking=True)
    button_style_coat = fields.Selection(
        [
            ("2button", "۲ بٹن"),
            ("3button", "۳ بٹن"),
        ],
        string="بٹن کی تعداد",
        tracking=True,
    )
    double_silai_coat = fields.Char(string="ڈبل سلائی", tracking=True)
    additional_notes_coat = fields.Char(string="اضافی نوٹس", tracking=True)

    # =========================
    # Misc / Global
    # =========================
    double_cuff_misc = fields.Char(string="ڈبل کف", tracking=True)
    paiping_wala = fields.Char(string="پائپنگ والا", tracking=True)
    front_pati = fields.Char(string="فرنٹ پٹی", tracking=True)
    mondha_tayar = fields.Char(string="مونڈھا تیار", tracking=True)
    half_button = fields.Char(string="ہاف بٹن", tracking=True)
    gol_kameez_misc = fields.Char(string="گول قمیض", tracking=True)
    collar_misc = fields.Char(string="کالر", tracking=True)
    cuff_misc = fields.Char(string="کف", tracking=True)
    samne_pocket = fields.Char(string="سامنے پاکٹ", tracking=True)
    shalwar_pocket = fields.Char(string="شلوار پاکٹ", tracking=True)
    seedhi_qameez = fields.Char(string="سیدھی قمیض", tracking=True)
    ban_misc = fields.Char(string="بین", tracking=True)
    bazu_misc = fields.Char(string="بازو", tracking=True)
    side_pocket = fields.Char(string="سائیڈ پاکٹ", tracking=True)
    contras_piece = fields.Char(string="کنٹراس پیس", tracking=True)
    additional_notes_misc = fields.Char(string="اضافی نوٹس", tracking=True)

    tailor_serial_number = fields.Char(
        string="سیریل نمبر",
        tracking=True,
        copy=False,
        readonly=True,
        index=True,
    )

    @api.model_create_multi
    def create(self, vals_list):
        """Assign tailor_serial_number only when specific context is present."""
        use_tailor_sequence = self.env.context.get('tailor_customer_sequence')
        if use_tailor_sequence:
            seq = self.env['ir.sequence'].next_by_code('tailor.customer.serial')
            # If next_by_code returns None once, we still want unique values per record
            for vals in vals_list:
                vals.setdefault(
                    'tailor_serial_number',
                    self.env['ir.sequence'].next_by_code('tailor.customer.serial') or seq or '/',
                )
        return super().create(vals_list)
