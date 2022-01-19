import os
rom_file = open("baserom.us.z64", "rb")

def main():
    def read_at(offset, size):
        rom_file.seek(int(offset))
        return rom_file.read(int(size))

    if not os.path.exists("sequences"):
        os.makedirs("sequences")

    def extract_file(filename,offset,length):
        with open(os.path.join("sequences",filename), "wb") as file:
            file.write(read_at(offset,length))

    extract_file("00_sound_player.m64",8063360,13452)
    extract_file("01_cutscene_collect_star.m64",8076816,619)
    extract_file("02_menu_title_screen.m64",8077440,8254)
    extract_file("03_level_grass.m64",8085696,5122)
    extract_file("04_level_inside_castle.m64",8090832,2494)
    extract_file("05_level_water.m64",8093328,4780)
    extract_file("06_level_hot.m64",8098112,2451)
    extract_file("07_level_boss_koopa.m64",8100576,3418)
    extract_file("08_level_snow.m64",8104000,8143)
    extract_file("09_level_slide.m64",8112144,7432)
    extract_file("0A_level_spooky.m64",8119584,5674)
    extract_file("0B_event_piranha_plant.m64",8125264,1395)
    extract_file("0C_level_underground.m64",8126672,4887)
    extract_file("0D_menu_star_select.m64",8131568,134)
    extract_file("0E_event_powerup.m64",8131712,3129)
    extract_file("0F_event_metal_cap.m64",8134848,2770)
    extract_file("10_event_koopa_message.m64",8137632,552)
    extract_file("11_level_koopa_road.m64",8138192,4741)
    extract_file("12_event_high_score.m64",8142944,271)
    extract_file("13_event_merry_go_round.m64",8143216,1657)
    extract_file("14_event_race.m64",8144880,197)
    extract_file("15_cutscene_star_spawn.m64",8145088,644)
    extract_file("16_event_boss.m64",8145744,3435)
    extract_file("17_cutscene_collect_key.m64",8149184,671)
    extract_file("18_event_endless_stairs.m64",8149856,1777)
    extract_file("19_level_boss_koopa_final.m64",8151648,3515)
    extract_file("1A_cutscene_credits.m64",8155168,14313)
    extract_file("1B_event_solve_puzzle.m64",8169488,216)
    extract_file("1C_event_toad_message.m64",8169712,208)
    extract_file("1D_event_peach_message.m64",8169920,432)
    extract_file("1E_cutscene_intro.m64",8170352,1764)
    extract_file("1F_cutscene_victory.m64",8172128,2058)
    extract_file("20_cutscene_ending.m64",8174192,1882)
    extract_file("21_menu_file_select.m64",8176080,781)
    extract_file("22_cutscene_lakitu.m64",8176864,313)


if __name__ == '__main__':
    main()
