#!/usr/bin/env python3
"""
Test script to verify GPT configuration
"""
import os
import sys
import yaml

def test_env_file():
    """Test .env file configuration"""
    env_file = '.env'
    if os.path.exists(env_file):
        print("✅ .env file exists")
        with open(env_file, 'r') as f:
            content = f.read()
            if 'OPENAI_API_KEY=' in content and 'sk-' in content:
                print("✅ .env file contains API key")
                return True
            else:
                print("❌ .env file missing or invalid API key")
                return False
    else:
        print("❌ .env file not found")
        return False

def test_config_yaml():
    """Test config.yaml configuration"""
    config_file = 'config.yaml'
    if os.path.exists(config_file):
        print("✅ config.yaml file exists")
        try:
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                api_key = config.get('openai', {}).get('api_key')
                if api_key and api_key.startswith('sk-'):
                    print("✅ config.yaml contains valid API key")
                    model = config.get('openai', {}).get('model', 'not set')
                    print(f"✅ Model configured: {model}")
                    return True
                else:
                    print("❌ config.yaml missing or invalid API key")
                    return False
        except Exception as e:
            print(f"❌ Error reading config.yaml: {e}")
            return False
    else:
        print("❌ config.yaml file not found")
        return False

def test_gitignore():
    """Test .gitignore protection"""
    gitignore_file = '.gitignore'
    if os.path.exists(gitignore_file):
        with open(gitignore_file, 'r') as f:
            content = f.read()
            if '.env' in content:
                print("✅ .env is protected in .gitignore")
                return True
            else:
                print("❌ .env is NOT protected in .gitignore")
                return False
    else:
        print("❌ .gitignore file not found")
        return False

def test_gpt_enhancer():
    """Test GPT enhancer can load configuration"""
    try:
        sys.path.append('scripts')
        from gpt_enhancer import GPTEnhancer
        
        enhancer = GPTEnhancer(base_dir='.')
        if enhancer.api_key:
            print(f"✅ GPT enhancer successfully loaded API key: {enhancer.api_key[:10]}...")
            return True
        else:
            print("❌ GPT enhancer could not load API key")
            return False
    except Exception as e:
        print(f"❌ Error testing GPT enhancer: {e}")
        return False

def main():
    print("🔍 Testing GPT Configuration...\n")
    
    tests = [
        ("Environment file", test_env_file),
        ("Config YAML", test_config_yaml),  
        ("Git protection", test_gitignore),
        ("GPT enhancer", test_gpt_enhancer)
    ]
    
    results = []
    for name, test_func in tests:
        print(f"\n📋 Testing {name}:")
        results.append(test_func())
    
    print(f"\n🎯 Summary: {sum(results)}/{len(results)} tests passed")
    
    if all(results):
        print("🎉 All configuration tests passed! GPT integration is ready.")
    else:
        print("⚠️ Some configuration issues found. Check the output above.")

if __name__ == "__main__":
    main()
