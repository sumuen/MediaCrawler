import pandas as pd
from typing import List, Dict, Tuple

def read_keywords_from_excel(file_path: str) -> List[Tuple[str, str]]:
    """
    从Excel文件中读取关键词和景点ID
    
    Args:
        file_path: Excel文件路径
        
    Returns:
        包含(景点ID, 英文关键词)元组的列表
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path)
        
        # 确保必要的列存在
        if 'attraction_id' not in df.columns or 'english_keywords' not in df.columns:
            raise ValueError("Excel文件必须包含'attraction_id'和'english_keywords'列")
        
        # 提取景点ID和英文关键词
        keyword_pairs = []
        for _, row in df.iterrows():
            attraction_id = str(row['attraction_id'])
            english_keywords = str(row['english_keywords'])
            if english_keywords and not pd.isna(english_keywords):
                keyword_pairs.append((attraction_id, english_keywords))
        
        return keyword_pairs
    except Exception as e:
        print(f"读取Excel文件时出错: {e}")
        return [] 