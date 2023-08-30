from django.db import models
from django.utils.translation import gettext_lazy as _


class Chassis(models.Model):
    """
    Stores a single Chassis
    """

    class TechnicalValues(models.TextChoices):
        WITH = "W", _("With")
        WITHOUT = "WO", _("Without")
        NOTVALID = "NV", _("Not valid")
        EGR = "STEPS", _("one step")


    vin = models.CharField('VIN', max_length=17)
    entry_into_service = models.DateField('Date of entry into service', auto_now=False, auto_now_add=False)
    assembly_date = models.DateField('Assembly date', auto_now=False, auto_now_add=False)
    type = models.CharField('Type', max_length=14)    
    series_truck = models.CharField('Series truck', max_length=11)
    # 0 General
    assembly_level = models.CharField('Assembly level', max_length=256)
    product_class = models.CharField('Product class', max_length=256)
    development_level = models.CharField('Development level', max_length=256)
    wheel_configuration = models.CharField('Wheel configuration', max_length=256)
    front_wheel_drive = models.BooleanField('Front wheel drive', default=False)
    axle_distance = models.IntegerField('Axle distance')
    chassis_width = models.IntegerField('Chassis width')
    plate_language = models.CharField('Plate language', max_length=64, default='English')
    axle_weight_front_technical = models.IntegerField('Axle weight front, technical', default=7500)
    axle_load_rear_technical = models.IntegerField('Axle load real, technical', default=11500)
    total_weight_technical = models.IntegerField('Total weight, technical', default=19000)
    technical_max_axle_weight_1st = models.IntegerField('Technical max axle weight 1st axle', default=7500)
    technical_weight_2nd = models.IntegerField('Technical weight on 2nd axle', default=11500)
    technical_weight_3rd = models.CharField('Technical weight on 3th axle', max_length=12, choices=TechnicalValues.choices, default=TechnicalValues.NOTVALID)
    technical_weight_4th = models.CharField('Technical weight on 4th axle', max_length=12, choices=TechnicalValues.choices, default=TechnicalValues.NOTVALID)
    technical_weight_5th = models.CharField('Technical weight on 5th axle', max_length=12, choices=TechnicalValues.choices, default=TechnicalValues.NOTVALID)
    max_axle_weight_1st_legal = models.CharField('Max legal axle weight on 1st axle', max_length=12, choices=TechnicalValues.choices, default=TechnicalValues.WITHOUT)
    max_axle_weight_2nd_legal = models.CharField('Max legal axle weight on 1st axle', max_length=12, choices=TechnicalValues.choices, default=TechnicalValues.WITHOUT)
    max_axle_weight_3rd_legal = models.CharField('Max legal axle weight on 1st axle', max_length=12, choices=TechnicalValues.choices, default=TechnicalValues.WITHOUT)    
    gross_vehicle_weight_legal = models.CharField('Gross vehicle weight, legal', max_length=64, choices=TechnicalValues.choices, default=TechnicalValues.WITHOUT)
    gross_trailer_weight_technical = models.IntegerField('GTW Technical', default=70000)
    gross_train_weight_legal = models.CharField('Gross train weight, legal', max_length=64, choices=TechnicalValues.choices, default=TechnicalValues.WITHOUT)
    preparation_tool_collect = models.CharField('Plate language', max_length=64, choices=TechnicalValues.choices, default=TechnicalValues.WITH)
    # 1 Engine
    stroke_volume = models.IntegerField('Engine stroke volume') 
    power_code = models.IntegerField('Power code', default=410)
    engine_type = models.CharField('Engine type/vehicle', max_length=32)
    engine_type_symbol = models.CharField('Engine type symbol', max_length=32)
    engine_serial_no = models.IntegerField('Engine stroke volume') 
    cylinder_block_generation = models.IntegerField('Cylinder block generation') 
    engine_speed_limit_with_low_oil_pressure = models.CharField('Engine speed limit with low oil pressure', max_length=32, choices=TechnicalValues.choices, default=TechnicalValues.WITHOUT)
    egr = models.CharField('EGR system', max_length=64, choices=TechnicalValues.choices, default=TechnicalValues.WITH)
    egr_cooling = models.CharField('EGR system cooling', max_length=64, choices=TechnicalValues.choices, default=TechnicalValues.WITH)

    class Meta:
        ordering = ["vin"]

    def __str__(self): 
        return self.vin

    # 0 General
    def truck_model(self):
        return self.vin[0:1]
    
    def type_of_transport(self):
        return self.vin[4:5]    
    
    def chassis_adaptation(self):
        return self.vin[5:6]
    
    def duty_class(self):
        return self.vin[9:10]
    
    def chassis_height(self):
        return self.vin[10:11]


class FFU(models.Model):
    """
    Stores a single FFU number relative to Chassis
    """
    category = models.ForeignKey(Chassis, related_name='ffu_number', on_delete=models.CASCADE)
    number = models.CharField(max_length=6)
    designation = models.CharField(max_length=256)


class LocalModifications(models.Model):
    """
    Stores a single Local Modifications number relative to Chassis
    """
    category = models.ForeignKey(Chassis, related_name='local_modifications', on_delete=models.CASCADE)
    designation = models.CharField(max_length=256)
