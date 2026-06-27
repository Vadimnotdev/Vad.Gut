from VadGutTitan.Logic.DataStream.ChecksumEncoder import ChecksumEncoder
from VadGutLogic.Message.LogicAvatarChange.LogicAvatarChange import LogicAvatarChange

SHOP_ITEMS = {
    "sh_g_magop0":  (0, "wp_magnum0", 10),
    "sh_g_sprayer0":(0, "wp_smg0", 10),
    "sh_g_bbuster0":(0, "wp_launcher0",10),
    "sh_g_bstik0":  (0, "wp_shotgun0", 10),
    "sh_g_fragball0":(1,"it_grenade0", 10),
    "sh_g_sdrone0": (1, "it_sdrone0", 10),
    "sh_g_bandage0":(1, "it_medikit0", 10),
    "sh_g_shield0": (2, "gd_armor0", 10),
    "sh_g_energy0": (2, "gd_energy0", 10),
    "sh_g_goggle0": (2, "gd_eyes0", 10),
    "sh_h_magop0":  (3, "hb_magnum0", 1),
    "sh_h_sprayer0":(3, "hb_smg0", 1),
    "sh_h_bbuster0":(3, "hb_launcher0", 1),
    "sh_h_bstik0":  (3, "hb_shotgun0", 1),
    "sh_h_fragball0":(3,"hb_grenade0", 1),
    "sh_h_sdrone0": (3, "hb_spydrone0", 1),
    "sh_h_bandage0":(3, "hb_medkit0", 1),
    "sh_h_shield0": (3, "hb_armor0", 1),
    "sh_h_energy0": (3, "hb_energy0", 1),
    "sh_h_goggle0": (3, "hb_eyes0", 1),
    "sh_b_mbag0":   (6, "mb_b0", 1),
    "sh_b_mbag1":   (6, "mb_b1", 1),
    "sh_b_mbag2":   (6, "mb_b2", 1),
    "sh_b_mbag3":   (6, "mb_b3", 1),
}
class LogicInventoryAvatarChange(LogicAvatarChange):
    def __init__(self, ShopId):
        super().__init__()
        categoryId, itemName, itemCount = SHOP_ITEMS[ShopId]
        self.CategoryId = categoryId
        self.InventoryItemCount = itemCount
        self.ItemName = itemName


    def encode(self, encoder: ChecksumEncoder):
        super().encode(encoder)
        encoder.writeInt(self.CategoryId)
        encoder.writeInt(self.InventoryItemCount)
        encoder.writeString(self.ItemName)
    
    def getAvatarChangeType(self):
        return 3