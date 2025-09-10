"""
API Server for Chess Gender Inequality Research Pipeline

This script runs a standalone API server that provides access to the research results.
"""

import os
import sys
import json
import sqlite3
import pandas as pd
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database path
DB_PATH = os.path.join('database', 'research_data.db')
EXPORTS_PATH = os.path.join('exports')

def get_latest_run_id():
    """Get the latest run_id from the database"""
    if not os.path.exists(DB_PATH):
        return None
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT run_id FROM runs ORDER BY timestamp DESC LIMIT 1")
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return result[0]
        return None
    except Exception as e:
        print(f"Error getting latest run: {str(e)}")
        return None

def get_papers_for_run(run_id):
    """Get all papers for a specific run"""
    if not os.path.exists(DB_PATH):
        return []
    
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query(
            "SELECT * FROM papers WHERE run_id = ?", 
            conn, 
            params=(run_id,)
        )
        conn.close()
        return df.to_dict(orient='records')
    except Exception as e:
        print(f"Error getting papers: {str(e)}")
        return []

@app.route('/')
def home():
    """Home page with API documentation"""
    return """
    <h1>Chess Gender Inequality Research API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li><a href="/api/runs">/api/runs</a> - List all research runs</li>
        <li><a href="/api/latest">/api/latest</a> - Get latest research results</li>
        <li>/api/run/{run_id} - Get results for a specific run</li>
        <li>/api/exports - List available export files</li>
        <li>/api/export/{filename} - Download a specific export file</li>
    </ul>
    """

@app.route('/api/runs')
def get_runs():
    """Get all research runs"""
    if not os.path.exists(DB_PATH):
        return jsonify({
            'status': 'error',
            'message': 'No database found'
        }), 404
    
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM runs ORDER BY timestamp DESC", conn)
        conn.close()
        return jsonify({
            'status': 'success',
            'runs': df.to_dict(orient='records')
        })
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/api/latest')
def get_latest():
    """Get the latest research results"""
    run_id = get_latest_run_id()
    if not run_id:
        return jsonify({
            'status': 'error',
            'message': 'No runs found'
        }), 404
    
    papers = get_papers_for_run(run_id)
    return jsonify({
        'status': 'success',
        'run_id': run_id,
        'papers': papers
    })

@app.route('/api/run/<run_id>')
def get_run(run_id):
    """Get results for a specific run"""
    papers = get_papers_for_run(run_id)
    if not papers:
        return jsonify({
            'status': 'error',
            'message': f'No results found for run {run_id}'
        }), 404
    
    return jsonify({
        'status': 'success',
        'run_id': run_id,
        'papers': papers
    })

@app.route('/api/exports')
def list_exports():
    """List all export files"""
    if not os.path.exists(EXPORTS_PATH):
        return jsonify({
            'status': 'error',
            'message': 'Exports directory not found'
        }), 404
    
    files = []
    for filename in os.listdir(EXPORTS_PATH):
        filepath = os.path.join(EXPORTS_PATH, filename)
        if os.path.isfile(filepath):
            files.append({
                'filename': filename,
                'size': os.path.getsize(filepath),
                'modified': os.path.getmtime(filepath)
            })
    
    return jsonify({
        'status': 'success',
        'files': files
    })

@app.route('/api/export/<path:filename>')
def download_export(filename):
    """Download a specific export file"""
    return send_from_directory(EXPORTS_PATH, filename, as_attachment=True)

if __name__ == '__main__':
    print("Starting Chess Gender Inequality Research API server...")
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
