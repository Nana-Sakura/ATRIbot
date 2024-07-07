
import ATRIproxy as Core


class QQ:
    def __init__(self):
        self.proxy = Core.ATRI()

    async def qq_get_user_id(self, qq_id, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        return await self.proxy.get_user(osuname)

    async def qq_get_bplists(self, qq_id, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        return await self.proxy.get_bplists(osuname)

    async def qq_get_bind(self, qq_id, osuname=None):
        return await self.proxy.update_bind_qq(qq_id, osuname)

    def qq_get_group_bind(self, group_id, members_list):
        return self.proxy.update_bind_group(group_id, members_list)

    async def qq_get_choke(self, qq_id, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"
        try:
            return await self.proxy.get_choke(osuname)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_if_add_pp(self, qq_id, pp_list, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        return await self.proxy.get_if_add_pp(osuname, pp_list)

    async def qq_get_avg_pp(self, qq_id, pp_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        return await self.proxy.get_avg_pp(osuname, pp_range)

    async def qq_get_avg_tth(self, qq_id, tth_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        return await self.proxy.get_avg_tth(osuname, tth_range)

    async def qq_get_avg_pt(self, qq_id, pt_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        return await self.proxy.get_avg_pt(osuname, pt_range)

    async def qq_get_bpsim(self, qq_id, pp_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        return await self.proxy.get_bpsim(osuname, pp_range)

    async def qq_get_bpsim_group(self, group_id, qq_id, pp_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        try:
            return await self.proxy.get_bpsim_group(group_id, osuname, pp_range)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_bpsimvs(self, qq_id, vs_name, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        try:
            return await self.proxy.get_bpsimvs(osuname, vs_name)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_join_date(self, group_id, qq_id, pp_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"
        try:
            return await self.proxy.get_join_date(group_id, osuname, pp_range)
        except ValueError:
            return "错误 尝试输入 !getgroups更新群成员列表"
        except Exception as e:
            return f'error: {e}'

    async def qq_get_group_ppmap(self, group_id, qq_id, pp_range, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"
        
        try:
            return await self.proxy.get_group_ppmap(group_id, osuname, pp_range)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_ptt_pp(self, qq_id, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"
        
        try:
            return await self.proxy.get_ptt_pp(osuname)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_tdba(self, qq_id, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"
        
        try:
            return await self.proxy.get_tdba(osuname)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_tdbavs(self, qq_id, vsname, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        return await self.proxy.get_tdbavs(osuname, vsname)

    async def qq_get_pr(self, qq_id, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        try:
            return await self.proxy.get_pr(osuname)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_brk(self, qq_id, group_id, beatmap_id, mods_list, osuname=None):

        if osuname is None:
            osuname = self.proxy.find_bind_name_qq(qq_id)

        if osuname is None:
            return "请先绑定输入 !getbind 你的osu用户名"

        try:
            return await self.proxy.get_brk(osuname, group_id, beatmap_id, mods_list)
        except Exception as e:
            return f'error: {e}'

    async def qq_get_brkup(self, beatmap_id, group_id):

        try:
            return await self.proxy.get_brkup(beatmap_id, group_id)
        except Exception as e:
            return f'error: {e}'
