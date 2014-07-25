# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BillAnalysisTbl(models.Model):
    analysis_id = models.DecimalField(primary_key=True, max_digits=22, decimal_places=0)
    bill_id = models.CharField(max_length=20)
    house = models.CharField(max_length=1, blank=True)
    analysis_type = models.CharField(max_length=100, blank=True)
    committee_code = models.CharField(max_length=6, blank=True)
    committee_name = models.CharField(max_length=200, blank=True)
    amendment_author = models.CharField(max_length=100, blank=True)
    analysis_date = models.DateTimeField(blank=True, null=True)
    amendment_date = models.DateTimeField(blank=True, null=True)
    page_num = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    source_doc = models.TextField(blank=True)
    released_floor = models.CharField(max_length=1, blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=20, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bill_analysis_tbl'


class BillDetailVoteTbl(models.Model):
    bill_id = models.CharField(max_length=20)
    location_code = models.CharField(max_length=6)
    legislator_name = models.CharField(max_length=50)
    vote_date_time = models.DateTimeField()
    vote_date_seq = models.IntegerField()
    vote_code = models.CharField(max_length=5, blank=True)
    motion_id = models.IntegerField()
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    member_order = models.IntegerField(blank=True, null=True)
    session_date = models.DateTimeField(blank=True, null=True)
    speaker = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'bill_detail_vote_tbl'


class BillHistoryTbl(models.Model):
    bill_id = models.CharField(max_length=20, blank=True)
    bill_history_id = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    action_date = models.DateTimeField(blank=True, null=True)
    action = models.CharField(max_length=2000, blank=True)
    trans_uid = models.CharField(max_length=20, blank=True)
    trans_update_dt = models.DateTimeField(blank=True, null=True)
    action_sequence = models.IntegerField(blank=True, null=True)
    action_code = models.CharField(max_length=5, blank=True)
    action_status = models.CharField(max_length=60, blank=True)
    primary_location = models.CharField(max_length=60, blank=True)
    secondary_location = models.CharField(max_length=60, blank=True)
    ternary_location = models.CharField(max_length=60, blank=True)
    end_status = models.CharField(max_length=60, blank=True)
    class Meta:
        managed = False
        db_table = 'bill_history_tbl'


class BillMotionTbl(models.Model):
    motion_id = models.DecimalField(primary_key=True, max_digits=20, decimal_places=0)
    motion_text = models.CharField(max_length=250, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bill_motion_tbl'


class BillSummaryVoteTbl(models.Model):
    bill_id = models.CharField(max_length=20)
    location_code = models.CharField(max_length=6)
    vote_date_time = models.DateTimeField()
    vote_date_seq = models.IntegerField()
    motion_id = models.IntegerField()
    ayes = models.IntegerField(blank=True, null=True)
    noes = models.IntegerField(blank=True, null=True)
    abstain = models.IntegerField(blank=True, null=True)
    vote_result = models.CharField(max_length=6, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    file_item_num = models.CharField(max_length=10, blank=True)
    file_location = models.CharField(max_length=50, blank=True)
    display_lines = models.CharField(max_length=2000, blank=True)
    session_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bill_summary_vote_tbl'


class BillTbl(models.Model):
    bill_id = models.CharField(primary_key=True, max_length=19)
    session_year = models.CharField(max_length=8)
    session_num = models.CharField(max_length=2)
    measure_type = models.CharField(max_length=4)
    measure_num = models.IntegerField()
    measure_state = models.CharField(max_length=40)
    chapter_year = models.CharField(max_length=4, blank=True)
    chapter_type = models.CharField(max_length=10, blank=True)
    chapter_session_num = models.CharField(max_length=2, blank=True)
    chapter_num = models.CharField(max_length=10, blank=True)
    latest_bill_version_id = models.CharField(max_length=30, blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    current_location = models.CharField(max_length=200, blank=True)
    current_secondary_loc = models.CharField(max_length=60, blank=True)
    current_house = models.CharField(max_length=60, blank=True)
    current_status = models.CharField(max_length=60, blank=True)
    days_31st_in_print = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bill_tbl'


class BillVersionAuthorsTbl(models.Model):
    bill_version_id = models.CharField(max_length=30)
    type = models.CharField(max_length=15)
    house = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    contribution = models.CharField(max_length=100, blank=True)
    committee_members = models.CharField(max_length=2000, blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    primary_author_flg = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'bill_version_authors_tbl'


class BillVersionTbl(models.Model):
    bill_version_id = models.CharField(primary_key=True, max_length=30)
    bill_id = models.CharField(max_length=19)
    version_num = models.IntegerField()
    bill_version_action_date = models.DateTimeField()
    bill_version_action = models.CharField(max_length=100, blank=True)
    request_num = models.CharField(max_length=10, blank=True)
    subject = models.CharField(max_length=1000, blank=True)
    vote_required = models.CharField(max_length=100, blank=True)
    appropriation = models.CharField(max_length=3, blank=True)
    fiscal_committee = models.CharField(max_length=3, blank=True)
    local_program = models.CharField(max_length=3, blank=True)
    substantive_changes = models.CharField(max_length=3, blank=True)
    urgency = models.CharField(max_length=3, blank=True)
    taxlevy = models.CharField(max_length=3, blank=True)
    bill_xml = models.TextField(blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bill_version_tbl'


class CodesTbl(models.Model):
    code = models.CharField(max_length=5, blank=True)
    title = models.CharField(max_length=2000, blank=True)
    class Meta:
        managed = False
        db_table = 'codes_tbl'


class CommitteeHearingTbl(models.Model):
    bill_id = models.CharField(max_length=20, blank=True)
    committee_type = models.CharField(max_length=2, blank=True)
    committee_nr = models.IntegerField(blank=True, null=True)
    hearing_date = models.DateTimeField(blank=True, null=True)
    location_code = models.CharField(max_length=6, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update_date = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'committee_hearing_tbl'


class DailyFileTbl(models.Model):
    bill_id = models.CharField(max_length=20, blank=True)
    location_code = models.CharField(max_length=6, blank=True)
    consent_calendar_code = models.IntegerField(blank=True, null=True)
    file_location = models.CharField(max_length=6, blank=True)
    publication_date = models.DateTimeField(blank=True, null=True)
    floor_manager = models.CharField(max_length=100, blank=True)
    trans_uid = models.CharField(max_length=20, blank=True)
    trans_update_date = models.DateTimeField(blank=True, null=True)
    session_num = models.CharField(max_length=2, blank=True)
    status = models.CharField(max_length=200, blank=True)
    class Meta:
        managed = False
        db_table = 'daily_file_tbl'


class LawSectionTbl(models.Model):
    id = models.CharField(max_length=100, blank=True)
    law_code = models.CharField(max_length=5, blank=True)
    section_num = models.CharField(max_length=30, blank=True)
    op_statues = models.CharField(max_length=10, blank=True)
    op_chapter = models.CharField(max_length=10, blank=True)
    op_section = models.CharField(max_length=20, blank=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    law_section_version_id = models.CharField(max_length=100, blank=True)
    division = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    part = models.CharField(max_length=100, blank=True)
    chapter = models.CharField(max_length=100, blank=True)
    article = models.CharField(max_length=100, blank=True)
    history = models.CharField(max_length=1000, blank=True)
    content_xml = models.TextField(blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'law_section_tbl'


class LawTocSectionsTbl(models.Model):
    id = models.CharField(max_length=100, blank=True)
    law_code = models.CharField(max_length=5, blank=True)
    node_treepath = models.CharField(max_length=100, blank=True)
    section_num = models.CharField(max_length=30, blank=True)
    section_order = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    title = models.CharField(max_length=400, blank=True)
    op_statues = models.CharField(max_length=10, blank=True)
    op_chapter = models.CharField(max_length=10, blank=True)
    op_section = models.CharField(max_length=20, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    law_section_version_id = models.CharField(max_length=100, blank=True)
    seq_num = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'law_toc_sections_tbl'


class LawTocTbl(models.Model):
    law_code = models.CharField(max_length=5, blank=True, primary_key=True)
    division = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    part = models.CharField(max_length=100, blank=True)
    chapter = models.CharField(max_length=100, blank=True)
    article = models.CharField(max_length=100, blank=True)
    heading = models.CharField(max_length=2000, blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    node_sequence = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    node_level = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    node_position = models.DecimalField(max_digits=22, decimal_places=0, blank=True, null=True)
    node_treepath = models.CharField(max_length=100, blank=True)
    contains_law_sections = models.CharField(max_length=1, blank=True)
    history_note = models.CharField(max_length=350, blank=True)
    op_statues = models.CharField(max_length=10, blank=True)
    op_chapter = models.CharField(max_length=10, blank=True)
    op_section = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'law_toc_tbl'


class LegislatorTbl(models.Model):
    district = models.CharField(max_length=5)
    session_year = models.CharField(max_length=8, blank=True)
    legislator_name = models.CharField(max_length=30, blank=True)
    house_type = models.CharField(max_length=1, blank=True)
    author_name = models.CharField(max_length=200, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    middle_initial = models.CharField(max_length=1, blank=True)
    name_suffix = models.CharField(max_length=12, blank=True)
    name_title = models.CharField(max_length=34, blank=True)
    web_name_title = models.CharField(max_length=34, blank=True)
    party = models.CharField(max_length=4, blank=True)
    active_flg = models.CharField(max_length=1)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    active_legislator = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'legislator_tbl'


class LocationCodeTbl(models.Model):
    session_year = models.CharField(max_length=8, blank=True)
    location_code = models.CharField(max_length=6)
    location_type = models.CharField(max_length=1)
    consent_calendar_code = models.CharField(max_length=2, blank=True)
    description = models.CharField(max_length=60, blank=True)
    long_description = models.CharField(max_length=200, blank=True)
    active_flg = models.CharField(max_length=1, blank=True)
    trans_uid = models.CharField(max_length=30, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    inactive_file_flg = models.CharField(max_length=1, blank=True)
    class Meta:
        managed = False
        db_table = 'location_code_tbl'


class VetoMessageTbl(models.Model):
    bill_id = models.CharField(max_length=20, blank=True)
    veto_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True)
    trans_uid = models.CharField(max_length=20, blank=True)
    trans_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'veto_message_tbl'

