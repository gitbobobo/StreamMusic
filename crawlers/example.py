#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
示例：如何使用播客爬虫
"""

from suancai import SuancaiCrawler
from wasai import WasaiCrawler


def example_suancai():
    """示例：爬取新闻酸菜馆播客"""
    print("=" * 60)
    print("示例 1: 爬取新闻酸菜馆播客")
    print("=" * 60)
    
    # 创建爬虫实例
    crawler = SuancaiCrawler()
    
    # 方法1: 自动搜索播客
    print("\n方法1: 自动搜索播客")
    podcast_id = crawler.search_podcast("新闻酸菜馆")
    
    if podcast_id:
        print(f"✓ 找到播客，ID: {podcast_id}")
        
        # 获取播客信息
        info = crawler.get_podcast_info(podcast_id)
        if info:
            print(f"  播客名称: {info.get('name')}")
            print(f"  节目总数: {info.get('programCount')}")
        
        # 爬取所有节目（实际使用时取消注释）
        # programs = crawler.crawl_all_programs(podcast_id)
        # crawler.save_to_json(programs, "suancai_programs.json")
        # crawler.generate_markdown(programs, "suancai_programs.md")
    else:
        print("✗ 未找到播客")
    
    # 方法2: 手动指定播客ID
    print("\n方法2: 手动指定播客ID")
    print("如果已知播客ID，可以直接使用：")
    print("crawler.podcast_id = '你的播客ID'")
    print("programs = crawler.crawl_all_programs()")


def example_wasai():
    """示例：爬取挖赛播客"""
    print("\n" + "=" * 60)
    print("示例 2: 爬取挖赛播客")
    print("=" * 60)
    
    # 创建爬虫实例
    crawler = WasaiCrawler()
    
    # 搜索播客
    print("\n搜索挖赛播客...")
    podcast_id = crawler.search_podcast("挖赛")
    
    if podcast_id:
        print(f"✓ 找到播客，ID: {podcast_id}")
        
        # 获取前10个节目作为示例
        print("\n获取节目列表（前10个）...")
        programs = crawler.get_program_list(podcast_id, limit=10)
        
        if programs:
            print(f"✓ 成功获取 {len(programs)} 个节目")
            
            # 解析并显示第一个节目的信息
            if programs:
                first_program = crawler.parse_program(programs[0])
                print("\n第一个节目信息:")
                print(f"  标题: {first_program['name']}")
                print(f"  时长: {first_program['duration_formatted']}")
                print(f"  发布时间: {first_program['create_time']}")
                print(f"  收听次数: {first_program['listen_count']}")
        else:
            print("✗ 未获取到节目列表")
    else:
        print("✗ 未找到播客")


def example_custom_output():
    """示例：自定义输出"""
    print("\n" + "=" * 60)
    print("示例 3: 自定义输出文件名")
    print("=" * 60)
    
    crawler = SuancaiCrawler()
    
    # 假设已经获取到节目列表
    mock_programs = [
        {
            'id': '1',
            'name': '示例节目',
            'description': '这是一个示例',
            'create_time': '2025-01-01 12:00:00',
            'duration': 1800,
            'duration_formatted': '30:00',
            'listen_count': 1000,
            'like_count': 50,
            'comment_count': 10,
            'audio_url': 'https://example.com/audio.mp3',
            'cover_url': 'https://example.com/cover.jpg'
        }
    ]
    
    # 保存到自定义文件名
    print("\n保存节目数据到自定义文件...")
    crawler.save_to_json(mock_programs, "my_custom_output.json")
    crawler.generate_markdown(mock_programs, "my_custom_output.md")
    print("✓ 数据已保存")


def main():
    """主函数"""
    print("播客爬虫使用示例\n")
    
    # 示例1: 爬取新闻酸菜馆
    example_suancai()
    
    # 示例2: 爬取挖赛
    example_wasai()
    
    # 示例3: 自定义输出
    example_custom_output()
    
    print("\n" + "=" * 60)
    print("所有示例运行完成！")
    print("=" * 60)
    print("\n提示：")
    print("1. 实际使用时请确保网络可以访问 music.163.com")
    print("2. 如需爬取完整数据，取消代码中的相关注释")
    print("3. 请遵守网易云音乐的使用条款")
    print("=" * 60)


if __name__ == '__main__':
    main()
