# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AgeGroup(models.Model):
    age_group_id = models.IntegerField(primary_key=True)
    age_group_desc = models.CharField(max_length=20, blank=True, null=True)
    age_group_start = models.DateField(blank=True, null=True)
    age_group_end = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'age_group'

class BattingStats(models.Model):
    player = models.OneToOneField('Player', models.DO_NOTHING, primary_key=True)
    plate_appearances = models.IntegerField(blank=True, null=True)
    at_bats = models.IntegerField(blank=True, null=True)
    sacrifices = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    home_runs = models.IntegerField(blank=True, null=True)
    singles = models.IntegerField(blank=True, null=True)
    doubles = models.IntegerField(blank=True, null=True)
    triples = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    walks = models.IntegerField(blank=True, null=True)
    hit_by_pitch = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'batting_stats'


class Coach(models.Model):
    coach_id = models.IntegerField(primary_key=True)
    coach_first = models.CharField(max_length=20, blank=True, null=True)
    coach_last = models.CharField(max_length=20, blank=True, null=True)
    coach_phone = models.IntegerField(blank=True, null=True)
    coach_email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coach'

class EmergencyContact(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    contact_first = models.CharField(max_length=20, blank=True, null=True)
    contact_last = models.CharField(max_length=20, blank=True, null=True)
    contact_number = models.IntegerField(blank=True, null=True)
    contact_email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'emergency_contact'


class FieldingStats(models.Model):
    player = models.OneToOneField('Player', models.DO_NOTHING, primary_key=True)
    errors = models.IntegerField(blank=True, null=True)
    putouts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    total_chances = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fielding_stats'


class Inning(models.Model):
    match = models.ForeignKey('Match', models.DO_NOTHING, blank=True, null=True)
    inning_num = models.IntegerField(primary_key=True)
    home_hits = models.IntegerField(blank=True, null=True)
    home_runs = models.IntegerField(blank=True, null=True)
    home_errors = models.IntegerField(blank=True, null=True)
    away_hits = models.IntegerField(blank=True, null=True)
    away_runs = models.IntegerField(blank=True, null=True)
    away_errors = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inning'


class Manager(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    manager_first = models.CharField(max_length=20, blank=True, null=True)
    manager_last = models.CharField(max_length=20, blank=True, null=True)
    manager_phone = models.IntegerField(blank=True, null=True)
    manager_email = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manager'


class Match(models.Model):
    match_id = models.IntegerField(primary_key=True)
    home_team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True, related_name = 'home_team')
    away_team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True, related_name = 'away_team')
    match_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'match'


class PitchingStats(models.Model):
    player = models.OneToOneField('Player', models.DO_NOTHING, primary_key=True)
    hits_allowed = models.IntegerField(blank=True, null=True)
    runs_allowed = models.IntegerField(blank=True, null=True)
    earned_runs_allowed = models.IntegerField(blank=True, null=True)
    innings_thrown = models.IntegerField(blank=True, null=True)
    pitches_thrown = models.IntegerField(blank=True, null=True)
    strikes_thrown = models.IntegerField(blank=True, null=True)
    strike_outs = models.IntegerField(blank=True, null=True)
    walks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pitching_stats'


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)
    contact = models.ForeignKey(EmergencyContact, models.DO_NOTHING, blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class Staff(models.Model):
    manager = models.ForeignKey(Manager, models.DO_NOTHING, blank=True, null=True)
    coach = models.ForeignKey(Coach, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('Team', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    manager = models.ForeignKey(Manager, models.DO_NOTHING, blank=True, null=True)
    coach = models.ForeignKey(Coach, models.DO_NOTHING, blank=True, null=True)
    age_group = models.ForeignKey(AgeGroup, models.DO_NOTHING, blank=True, null=True)
    team_name = models.CharField(max_length=30, blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
