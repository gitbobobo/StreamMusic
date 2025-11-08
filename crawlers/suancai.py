#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
新闻酸菜馆播客爬虫
从网易云音乐爬取"新闻酸菜馆"播客内容
"""

import json
import requests
import time
from typing import List, Dict, Optional
from datetime import datetime


class SuancaiCrawler:
    """新闻酸菜馆播客爬虫类"""
    
    def __init__(self):
        """初始化爬虫"""
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://music.163.com/'
        })
        self.base_url = 'https://music.163.com'
        self.api_url = 'https://music.163.com/api'
        
        # 新闻酸菜馆的专辑/播客ID（需要根据实际情况填写）
        self.podcast_id = None  # 待填写实际的播客ID
        
    def search_podcast(self, keyword: str = "新闻酸菜馆") -> Optional[str]:
        """
        搜索播客
        
        Args:
            keyword: 搜索关键词
            
        Returns:
            播客ID或None
        """
        try:
            search_url = f"{self.api_url}/search/get"
            params = {
                's': keyword,
                'type': 1009,  # 1009表示播客类型
                'limit': 10,
                'offset': 0
            }
            
            response = self.session.get(search_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('result') and data['result'].get('djRadios'):
                    radios = data['result']['djRadios']
                    for radio in radios:
                        if keyword in radio.get('name', ''):
                            print(f"找到播客: {radio['name']}")
                            return str(radio['id'])
            else:
                print(f"搜索失败: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"搜索播客时出错: {str(e)}")
            
        return None
    
    def get_podcast_info(self, podcast_id: str) -> Optional[Dict]:
        """
        获取播客基本信息
        
        Args:
            podcast_id: 播客ID
            
        Returns:
            播客信息字典或None
        """
        try:
            url = f"{self.api_url}/djradio/v2/get"
            params = {'id': podcast_id}
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('data'):
                    return data['data']
            else:
                print(f"获取播客信息失败: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"获取播客信息时出错: {str(e)}")
            
        return None
    
    def get_program_list(self, podcast_id: str, limit: int = 100, offset: int = 0) -> List[Dict]:
        """
        获取播客节目列表
        
        Args:
            podcast_id: 播客ID
            limit: 每页数量
            offset: 偏移量
            
        Returns:
            节目列表
        """
        programs = []
        
        try:
            url = f"{self.api_url}/dj/program/byradio"
            params = {
                'radioId': podcast_id,
                'limit': limit,
                'offset': offset,
                'asc': 'false'  # false表示降序，最新的在前
            }
            
            response = self.session.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('programs'):
                    programs = data['programs']
            else:
                print(f"获取节目列表失败: HTTP {response.status_code}")
                
        except Exception as e:
            print(f"获取节目列表时出错: {str(e)}")
            
        return programs
    
    def parse_program(self, program: Dict) -> Dict:
        """
        解析节目信息
        
        Args:
            program: 原始节目数据
            
        Returns:
            格式化的节目信息
        """
        main_song = program.get('mainSong', {})
        
        parsed = {
            'id': program.get('id'),
            'name': program.get('name', ''),
            'description': program.get('description', ''),
            'create_time': datetime.fromtimestamp(
                program.get('createTime', 0) / 1000
            ).strftime('%Y-%m-%d %H:%M:%S'),
            'duration': main_song.get('duration', 0) // 1000,  # 转换为秒
            'duration_formatted': self._format_duration(main_song.get('duration', 0)),
            'listen_count': program.get('listenerCount', 0),
            'like_count': program.get('likedCount', 0),
            'comment_count': program.get('commentCount', 0),
            'audio_url': main_song.get('mp3Url', ''),
            'cover_url': program.get('coverUrl', '') or program.get('blurCoverUrl', ''),
        }
        
        return parsed
    
    def _format_duration(self, milliseconds: int) -> str:
        """
        格式化时长
        
        Args:
            milliseconds: 毫秒数
            
        Returns:
            格式化的时长字符串（MM:SS或HH:MM:SS）
        """
        seconds = milliseconds // 1000
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        
        if hours > 0:
            return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        else:
            return f"{minutes:02d}:{secs:02d}"
    
    def crawl_all_programs(self, podcast_id: Optional[str] = None) -> List[Dict]:
        """
        爬取所有节目
        
        Args:
            podcast_id: 播客ID，如果为None则使用默认ID
            
        Returns:
            所有节目的列表
        """
        if podcast_id is None:
            podcast_id = self.podcast_id
            
        if podcast_id is None:
            print("错误: 未指定播客ID")
            return []
        
        all_programs = []
        offset = 0
        limit = 100
        
        print(f"开始爬取播客 ID: {podcast_id}")
        
        while True:
            print(f"正在获取第 {offset // limit + 1} 页...")
            programs = self.get_program_list(podcast_id, limit=limit, offset=offset)
            
            if not programs:
                break
            
            for program in programs:
                parsed = self.parse_program(program)
                all_programs.append(parsed)
            
            print(f"已获取 {len(all_programs)} 个节目")
            
            # 如果返回的节目数少于limit，说明已经是最后一页
            if len(programs) < limit:
                break
            
            offset += limit
            time.sleep(1)  # 添加延迟，避免请求过快
        
        print(f"爬取完成，共 {len(all_programs)} 个节目")
        return all_programs
    
    def save_to_json(self, programs: List[Dict], filename: str = "suancai_programs.json"):
        """
        保存节目列表到JSON文件
        
        Args:
            programs: 节目列表
            filename: 文件名
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(programs, f, ensure_ascii=False, indent=2)
            print(f"数据已保存到 {filename}")
        except Exception as e:
            print(f"保存文件时出错: {str(e)}")
    
    def generate_markdown(self, programs: List[Dict], filename: str = "suancai_programs.md"):
        """
        生成Markdown格式的节目列表
        
        Args:
            programs: 节目列表
            filename: 文件名
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("# 新闻酸菜馆节目列表\n\n")
                f.write(f"更新时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                f.write(f"共 {len(programs)} 期节目\n\n")
                f.write("---\n\n")
                
                for i, program in enumerate(programs, 1):
                    f.write(f"## {i}. {program['name']}\n\n")
                    f.write(f"- **发布时间**: {program['create_time']}\n")
                    f.write(f"- **时长**: {program['duration_formatted']}\n")
                    f.write(f"- **收听次数**: {program['listen_count']}\n")
                    f.write(f"- **点赞数**: {program['like_count']}\n")
                    f.write(f"- **评论数**: {program['comment_count']}\n")
                    
                    if program.get('description'):
                        f.write(f"\n**简介**: {program['description']}\n")
                    
                    if program.get('cover_url'):
                        f.write(f"\n![封面]({program['cover_url']})\n")
                    
                    f.write("\n---\n\n")
            
            print(f"Markdown文件已保存到 {filename}")
        except Exception as e:
            print(f"生成Markdown文件时出错: {str(e)}")


def main():
    """主函数"""
    crawler = SuancaiCrawler()
    
    # 搜索"新闻酸菜馆"播客
    print("正在搜索'新闻酸菜馆'播客...")
    podcast_id = crawler.search_podcast("新闻酸菜馆")
    
    if podcast_id:
        # 获取播客信息
        print(f"\n正在获取播客信息...")
        podcast_info = crawler.get_podcast_info(podcast_id)
        
        if podcast_info:
            print(f"播客名称: {podcast_info.get('name')}")
            print(f"播客描述: {podcast_info.get('desc', '')[:100]}...")
            print(f"节目总数: {podcast_info.get('programCount', 0)}")
        
        # 爬取所有节目
        print(f"\n开始爬取所有节目...")
        programs = crawler.crawl_all_programs(podcast_id)
        
        if programs:
            # 保存为JSON
            crawler.save_to_json(programs)
            
            # 生成Markdown
            crawler.generate_markdown(programs)
            
            print(f"\n爬取完成!")
            print(f"共获取 {len(programs)} 期节目")
    else:
        print("未找到'新闻酸菜馆'播客，请手动指定播客ID")
        print("使用方法: crawler.podcast_id = '你的播客ID'")


if __name__ == '__main__':
    main()
