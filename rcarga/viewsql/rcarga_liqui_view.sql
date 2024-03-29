USE [CrmEuro]
GO


SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO



CREATE VIEW [dbo].[rcarga_liqui_view]
as
    SELECT T0.id, T1.id AS 'itemsid', T0.fecha, T0.total, T4.name as 'division', T1.docnum, T3.ruta, T2.estatus, T5.fechare, T5.docpago,
        T5.documentos, T5.reten, T5.pago, T1.cardname, T1.totalvalor

    FROM rcarga T0
        LEFT OUTER JOIN rcarga_item T1 ON T0.id=T1.rcarga_id
        INNER JOIN rcarga_estatus T2 ON T0.estatus_id=T2.id
        INNER JOIN rcarga_ruta T3 ON T0.ruta_id=T3.id
        INNER JOIN division T4 ON T0.division_id=T4.id
        LEFT JOIN rcarga_liqui T5 ON T1.id=T5.rcarga_item_id
        
        
GO


